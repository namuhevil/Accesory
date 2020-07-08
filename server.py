# -*- coding: utf-8 -*-
import socket
import numpy as np
HOST = '192.168.50.182'
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)
count = 0
data = np.zeros((1, 6))
while True:
    conn, addr = server.accept()
    clientMessage = str(conn.recv(1024), encoding='utf-8')

    #print('Client message is:', clientMessage)

    #serverMessage = 'I\'m here!'
    if(count%6 == 0):
        data[0][0] = clientMessage
    elif(count%6 == 1):
        data[0][1] = clientMessage
    elif(count%6 == 2):
        data[0][2] = clientMessage
    elif(count%6 == 3):
        data[0][3] = clientMessage
    elif(count%6 == 4):
        data[0][4] = clientMessage
    elif(count%6 == 5):
        data[0][5] = clientMessage
        print(data)
        count = 0

    count += 1

    #conn.sendall(serverMessage.encode())
    conn.close()