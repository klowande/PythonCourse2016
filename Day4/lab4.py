#Go to https://polisci.wustl.edu/faculty/specialization
#Go to the page for each of the professors.
#Create a .csv file with the following information for each professor:
# 	-Specialization *****
# 	-Name *****
# 	-Title
# 	-E-mail
# 	-Web page
	
from bs4 import BeautifulSoup
import urllib2 
import random
import time
import os
import re

web_address='https://polisci.wustl.edu/faculty/specialization'
web_page = urllib2.urlopen(web_address)

soup = BeautifulSoup(web_page.read())
soup.prettify()

# for loop that prints all names
names = soup.find_all('a',{'class':"person-view-primary-field" })
for i in names:
	print i.get_text()

# for loop that returns all fields
subfields=soup.find_all('h3')
for subfield in subfields:
	for sibling in subfield.next_siblings:
		if sibling in subfields:
			break
		else:
			print subfield.get_text()
			
# for loop that returns all names and ranks - can't get it to skip the names
ranks = soup.find_all('div',{'class':re.compile('views-row+.*') })
for rank in ranks:
	print rank.get_text(", ",strip=True)

# urls
urls = []
for link in ranks:
    urls.append(link.get('a'))

for site in urls:
	webpage = web_page + site
	print webpage







# gets a list of urls
urls = soup.find_all('href')
for j in urls:
	print j.get_text()
	

# children
content = soup.find_all('div',{'class':'view-content'})[0]
content.descendants
for j in content.children:
	print j
 # function that gets a name	
def Name(self):
	return soup.find_all('a',{'class':"person-view-primary-field" })[self].get_text()
	
# function that returns field
def Field(self):
	return soup.find_all('h3')[self].get_text()
    

