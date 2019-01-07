import zmq
import threading
import uuid
import time

bind_address = 'tcp://127.0.0.1:5000'

def publisher():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.connect(bind_address)
    pub_id = str(uuid.uuid4())
    message_number = 0
    print(f'Pub {pub_id} starting.')
    while True:
        socket.send_string(f"{pub_id} {message_number}")
        message_number += 1
        time.sleep(1)


def subscriber():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.bind(bind_address)
    socket.setsockopt_string(zmq.SUBSCRIBE, '')

    print('Starting sub thread.')
    while True:
        recv_msg = socket.recv()
        print(recv_msg)
        time.sleep(0.1)


sub_thread = threading.Thread(target=subscriber)

pub_threads = [threading.Thread(target=publisher) for _ in range(3)]

sub_thread.start()

for pub_thread in pub_threads:
    pub_thread.start()