from bs4 import BeautifulSoup as soup
f=open("scrapy.html","r")
raw=f.read()
source=soup(raw,"html5lib")
#Finding all the tag names present in the page
h=set()
for tag in source.find_all(True):
    h.add(tag.name)
m=list(h)
#title of the webpage
print(source.title.text)
#now extrcting all the paragraphs in the webpage
for k in source.find_all('p'):
	print(k.text)
#now extracting all the links in the webpage
for t in source.find_all('a'):
	print(t['href'])
#now extracting all the headings from div tags
for j in source.find_all('div'):
	for l in j.find_all('h3'):
		print(l.text)
#now extracting all the images
for j in source.find_all('div'):
	for l in j.find_all('h3'):
		print(l.text)

#now extracting all the lists
for j in source.find_all('div'):
	for l in j.find_all('ul'):
		for k in l.find_all('li'):
			print(k.text)


#now extracting header
for l in source.find_all('header'):
		print(l.text)

#now extracting footer
for j in source.find_all('footer'):
		print(j.text)
