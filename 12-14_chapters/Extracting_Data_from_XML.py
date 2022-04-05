# An assignment Extracting Data from XML

#Coursera. Using Python to Access Web Data. Week 5. 
#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
#The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract 
#the comment counts from the XML data, compute the sum of the numbers in the file.


from urllib import request
import xml.etree.ElementTree as ET


# url = 'http://py4e-data.dr-chuck.net/comments_1412580.xml'
url = input('enter a URL')
print ("Retrieving", url)
html = request.urlopen(url)
data = html.read()

tree = ET.fromstring(data)
sum = 0
counts = tree.findall('.//count')
print('User count:', len(counts))
for count in counts:
    sum += int(count.text)

print(sum)

