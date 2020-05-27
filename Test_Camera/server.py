import socket
import sys
import cv2
import pickle
import numpy as np
import struct

HOST = '192.168.22.23'
PORT = 8083

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST, PORT))
print('Socket bind complete')

s.listen(10)
print('Socket now listening')

#print('hello1')
conn, addr = s.accept()

#print('hello2')
data = b''
payload_size = struct.calcsize("i")

#print('hello3')


while True:
    while len(data) < payload_size:
        data += conn.recv(int(4096/0.5))
    packed_msg_size = data[:payload_size]

    data = data[payload_size:]
    msg_size = struct.unpack("i", packed_msg_size)[0]

    while len(data) < msg_size:
        data += conn.recv(int(4096/0.5))
    frame_data = data[:msg_size]
    data = data[msg_size:]
    #print('hello')
    frame=pickle.loads(frame_data)
    #print(frame.size)
    cv2.imshow('frame', frame)
    key = cv2.waitKey(10)
    if key == 27:
    	break

#cap.release()
cv2.destroyAllWindows()



