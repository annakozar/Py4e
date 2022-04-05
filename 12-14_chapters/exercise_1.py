#Change the socket program socket1.py to prompt the user for the URL so it can read any web page. 
#You can use split('/') to break the URL into its component parts so you can extract the host name 
#for the socket connect call. Add error checking using try and except to handle the condition where 
#the user enters an improperly formatted or non-existent URL.


import socket



url = input('http:// ')
host = url.split("/", 1)[0]

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = f'GET http://{url} HTTP/1.0\r\n\r\n'.encode()
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
except:
    quit()

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
