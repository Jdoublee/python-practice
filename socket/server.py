from socket import *

serverSock = socket(AF_INET, SOCK_STREAM) # AF_INET:IPv4, AF_INET6:IPv6 // SOCK_STREAM과 SOCK_DGRAM 주로 사용됨
serverSock.bind(('', 8080)) # 생성된 소켓의 번호와 실제 어드레스 패밀리를 연결. (ip,port) '':모든 인터페이스와 연결
serverSock.listen(1) # 동시접속 개수만큼 접속 기다림

connectionSock, addr = serverSock.accept() # accept():소켓에 누군가가 접속하여 연결되었을 때 결과값 return. 이후부터는 connectionSock만 사용
print(str(addr),'에서 접속이 확인되었습니다.')

data = connectionSock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8')) # decode(): 바이트를 문자열로 디코딩

connectionSock.send('I am a server.'.encode('utf-8')) # encode():문자열을 byte로 변환
print('메시지를 보냈습니다.')