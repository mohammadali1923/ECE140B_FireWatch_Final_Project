import cv2
import numpy as np
import socket
import sys
import pickle
import struct

cap = cv2.VideoCapture(0)
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('192.168.22.23', 8083))

while True:
    ret,frame = cap.read()
    dim = (400, 200)
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    data = pickle.dumps(frame)
    clientsocket.sendall(struct.pack("i", len(data)) + data)


