from bs4 import BeautifulSoup as soup
import urllib
import sys
page=urllib.request.urlopen("https://pagalworld.io/")
raw_html=page.read()
page.close()
source=soup(raw_html,'html.parser')
lis=source.contents
f=open("scrapy.html","w")
for k in lis:
	f.write(str(k))
f=open("scrapy.html","r")
hunt=f.read()
for k in hunt.splitlines():
	print(k)

