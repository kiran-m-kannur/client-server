import socket

# Initialize Socket Instance
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print ("Socket created successfully.")

# Defining port and host
port = 5566
host = 'localhost'

# Connect socket to the host and port
sock.connect((host, port))
print('Connection Established.')
# Send a greeting to the server
sock.sendall('A message from the client'.encode())

# Write File in binary
file = open('global_model.h5', 'wb')

# Keep receiving data from the server
line = sock.recv(1024)

while(line):
    file.write(line)
    line = sock.recv(1024)

print('File has been received successfully.')

file.close()
sock.close()
print('Connection Closed.')