import socket

ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ms.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0'.encode()
ms.send(cmd)

while True:
    data = ms.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
ms.close()
