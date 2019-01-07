import cv2
import base64
import time



cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    _, encoded_frame = cv2.imencode('.jpg', frame)
    print(base64.b64encode(encoded_frame.tobytes())[:100])
    cv2.imshow('', frame)
    cv2.waitKey(0)
    time.sleep(0.1)