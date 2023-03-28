import socket

HOST = '127.0.0.1'
PORT = 6677

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s :
    s.connect((HOST,PORT))
    s.sendall(b'Node 1 connected')
    data  = s.recv(1024)

print('Recived',repr (data))