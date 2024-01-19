#server

import socket

host = '10.10.10.5'
port = 8080

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

s.listen(5)

print("Waiting from incomming connection with Port:", port)

while True:
    conn,addr = s.accept()
    print("Got connection from ", addr)
    msg = "Hi This Server"
    conn.send(msg.encode())
    conn.close()