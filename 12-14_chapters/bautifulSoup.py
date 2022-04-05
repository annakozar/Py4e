#Scraping HTML Data with BeautifulSoup
#In this assignment you will write a Python program to use urllib to read the HTML from the data files below, 
#and parse the data, extracting numbers and compute the sum of the numbers in the file

#This  is an assignment from Coursera Using Python to Access Web Data: Week 4

from urllib.request import urlopen
#import below may be not working well if you are using linux nano 
from bs4 import BeautifulSoup
import ssl
summ_str = 0
amount = 0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    summ = tag.contents[0]
    summ_str += int(str(summ))

print(summ_str)

