#Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, 
#(2) displaying up to 3000 characters, and (3) counting the overall number of characters 
#in the document. Don’t worry about the headers for this exercise, simply show the first 
#3000 characters of the document contents.


import urllib.request, urllib.parse, urllib.error

data = ""
url = input('http:// ')
try:
    fhand = urllib.request.urlopen(f'http://{url}')
except:
    quit()

for line in fhand:

    words = line.decode()
    data += words

print(data[:2999])
print("this document contains ", len(data), "characters")
