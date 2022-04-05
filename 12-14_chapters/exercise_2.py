#Change your socket program so that it counts the number of characters it has received and stops 
#displaying any text after it has shown 3000 characters. The program should retrieve the entire 
#document and count the total number of characters and display the count of the number of 
#characters at the end of the document.

import socket

data = ""
url = input('http:// ')
host = url.split("/", 1)[0]

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = f'GET http://{url} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

except:
    quit()

while True:
    _ = mysock.recv(512).decode()
    data += _
    if len(_) < 1:
        break
print(data[:3000],end='')

print("this document contains ", len(data), "characters")
mysock.close()
