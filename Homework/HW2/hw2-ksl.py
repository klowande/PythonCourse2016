# scraping petitions.gov

# desired fields:
# title *
# signatures *
# policy areas *
# due date

from bs4 import BeautifulSoup
import urllib2 
import csv
import re

# open active .csv
f = open('wh-petitions.csv', 'wb')
writer = csv.DictWriter(f, fieldnames=("Title", "Signatures","Policy Areas"))
writer.writeheader()

# saved source code
pages = ['petitions-pg0.htm','petitions-pg1.htm','petitions-pg2.htm','petitions-pg3.htm']
 		
# master function to get petition info
def process_pet(div_tag):
	title=div_tag.find('h3').string
	signatures=div_tag.find('span',{'class':'signatures-number'}).string
	policy_areas=[]
	for i in div_tag.find_all('h6'):
		policy_areas.append(i.string)
	policies = ', '.join(policy_areas)
	writer.writerow({"Title":title.encode("utf-8"), "Signatures":signatures.encode("utf-8"),"Policy Areas":policies.encode("utf-8")}) 
	
# "Due Date":due_date['email']
# function to get due date from petition page
# def due_frompage(url):
#	pet_page=urllib2.urlopen(url)
#	pet_soup=BeautifulSoup(pet_page.read())
#	pet_date = 'NA'
#	div 

# iterate through all saved webpages and entries in each webpage
for webpg in pages:
	soup = BeautifulSoup(open(webpg))
	entries = soup.find_all('div',{'class':re.compile('views-row+.*') })
	for entry in entries:
		process_pet(entry)
 		
f.close()

# toy code #
