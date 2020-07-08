import socket
import numpy as np

HOST = '192.168.50.87'
PORT = 8000


a = 1
count = 0
while a > 0:


    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    if(count%6 == 0):
        clientMessage = '180'
        client.sendall(clientMessage.encode())
    elif(count%6 == 1):
        clientMessage = '43'
        client.sendall(clientMessage.encode())

    elif(count%6 == 2):
        clientMessage = '22'
        client.sendall(clientMessage.encode())
    
    elif(count%6 == 3):
        clientMessage = '133'
        client.sendall(clientMessage.encode())

    elif(count%6 == 4):
        clientMessage = '33'
        client.sendall(clientMessage.encode())

    elif(count%6 == 5):
        clientMessage = '143'
        client.sendall(clientMessage.encode())
        count = 0

    serverMessage = str(client.recv(1024), encoding='utf-8')
    count += 1

    print('Server:', serverMessage)

client.close()