
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

spans = soup('span')
x =  list()
sum = 0
for span in spans:
    y = span.contents[0]
    x.append(y)
for item in x:
    sum = sum + int(item)
print(sum)
