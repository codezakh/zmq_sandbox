import asyncio
import datetime
import random
import websockets
import cv2
import base64


cap = cv2.VideoCapture(0)

async def time(websocket, path):
    while True:
        ret, frame = cap.read()
        _, encoded_frame = cv2.imencode('.jpeg', frame)
        b64_payload = base64.b64encode(encoded_frame.tobytes()).decode('utf-8')
        await websocket.send(b64_payload)
        await asyncio.sleep(0.030)

start_server = websockets.serve(time, '10.20.0.160', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()