#Assignment: Following Links in HTML Using BeautifulSoup
#Coursera. Using Python to Access Web Data. Week 4.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
def do(url, count):
    for _ in range(count):
        links = []
        html = urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        tags = soup('a')
        for tag in tags:
            links.append(tag.get('href', None))
        url = links[2]
    return url
result = do(url, 4)
print(result)
x = result.split(".")
print(x[2].split("_")[2])

