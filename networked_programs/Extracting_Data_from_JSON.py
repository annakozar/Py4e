#an assignment Extracting Data from JSON
#Coursera. Using Python to Access Web Data. Week 6

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. 
#The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract 
#the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum 

import urllib.request, urllib.error
import json
import ssl

serviceurl = input('Enter URL- ')
count = 0
sum = 0


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


uh = urllib.request.urlopen(serviceurl, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None


for coment in js['comments']:
        count = count +1
        sum += coment['count']


print("sum:", sum)
print("count:", count)
