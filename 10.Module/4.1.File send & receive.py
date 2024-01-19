#client 

import socket

s = socket.socket()
host = "10.10.10.5"
port = 8080
s.connect((host,port))
print("Connected ..........")

#File receive

file = open('receive', 'web')
file_data = s.recv(1024)
file.close()

print("file has beeb received")