# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
# url - http://py4e-data.dr-chuck.net/comments_947808.html
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

## Retrieve all of the anchor tags
s=0
count = 0
l=list()
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    temp = int(tag.contents[0])
    #s = s + temp
    #print(temp)
    l.append(temp)
    count =count + 1

#print(count)
from functools import reduce
sum=reduce(lambda a,b:a+b, l)
print(sum)
