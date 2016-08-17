#Go to https://polisci.wustl.edu/faculty/specialization
#Go to the page for each of the professors.
#Create a .csv file with the following information for each professor:
# 	-Specialization *****
# 	-Name *****
# 	-Title *****
# 	-E-mail
# 	-Web page
	
from bs4 import BeautifulSoup
import urllib2 
import csv

web_address='https://polisci.wustl.edu/faculty/specialization'
web_page = urllib2.urlopen(web_address)

soup = BeautifulSoup(web_page.read())
soup.prettify()

names = []
titles = []
fields = []

faculty = soup.find_all('div',{'class':re.compile('views-row+.*') })
for i in range(0,len(faculty)):
	names.append(faculty[i].find('a').get_text())
	titles.append(faculty[i].contents[2])

subfields=soup.find_all('h3')
for subfield in subfields:
	for sibling in subfield.next_siblings:
		if sibling in subfields:
			break
		else:
			try:
				sibling.get_text()
				fields.append(subfield.get_text())
			except:
				pass

# writing the file
with open('wustl-faculty.csv', 'w') as f:
  my_writer = csv.DictWriter(f, fieldnames=("Name", "Title", "Field")) # variable names, determines order.
  my_writer.writeheader()
  for i in range(0, len(faculty)):
    my_writer.writerow({"Name": names[i], "Title": titles[i], "Field": fields[i]})
    
    