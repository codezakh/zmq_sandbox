import zmq


context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect("tcp://localhost:%s", % 1337)
socket.setsockopt_string(zmq.SUBSCRIBE)