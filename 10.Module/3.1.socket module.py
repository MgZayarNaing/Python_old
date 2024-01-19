# client

host = "10.10.10.5"
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
print (s.recv(1024).decode())
s.close()