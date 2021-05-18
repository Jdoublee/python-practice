from socket import *
from threading import *
import time

def send(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))

def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))


port = 8080

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('', port))

print('접속 완료')

sender = Thread(target=send, args=(clientSock,)) # target:실제로 실행할 함수, args:그 함수에 전달할 인자
receiver = Thread(target=receive, args=(clientSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass