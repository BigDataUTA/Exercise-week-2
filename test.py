from bs4 import BeautifulSoup
a = open("html_doc.html","rb")
soup = BeautifulSoup(a, 'html.parser')
b = soup.p
for i in b.children:
	
	print i.children
