# scraping petitions.gov

# desired fields:
# title *
# signatures *
# policy areas *
# due date

from bs4 import BeautifulSoup
import urllib2 
import csv

# open saved web page
webpg = 'petitions-pg1.htm'
soup = BeautifulSoup(open(webpg))

# open active .csv
with open('wh-petitions.csv', 'wb') as f:
	my_writer = csv.DictWriter(f, fieldnames=("Name", "Subfield","Title","E-mail","Web-page"))
	my_writer.writeheader()

# master function to get petition info
def process_pet(div_tag):
	title=div_tag.find('h3').string
	signatures=div_tag.find('span',{'class','signatures-number'}).string
	policy_areas=[]
	for i in div.tag.find_all('h6'):
		policy_areas.append(i.string)
	policies = ', '.join(policy_areas)
	url='https://petitions.whitehouse.gov/'+  # div_tag.find('h3')['href']
#	due_date=profinfo_frompage(prof_address)
	my_writer.writerow({"Title":title, "Signatures":subfield,"Policy Areas":policy_area,"Due Date":due_date['email']}) 

# function to get due date from petition page
# def due_frompage(url):
#	pet_page=urllib2.urlopen(url)
#	pet_soup=BeautifulSoup(pet_page.read())
#	pet_date = 'NA'
#	div 

# for loop to loop through each entry
# for i in soup.find_all('div',{'class':re.compile('views-row+.*') }):

f.close()


# toy code
soup.find_all('span',{'class': 'signatures-number' })

title=titles.find('h3').string

url='https://petitions.whitehouse.gov/'+soup.find_all('h3')['href']