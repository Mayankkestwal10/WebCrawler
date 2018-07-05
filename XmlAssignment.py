import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter location : ")
xml = urllib.request.urlopen(url).read()

tree = ET.fromstring(xml)

counts = tree.findall('comments/comment/count')

v = 0

for count in counts:
    v = v + int(count.text)

print('Total :',v)
