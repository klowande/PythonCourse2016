import re

# open text file of 2008 NH primary Obama speech
file = open("obama-nh.txt", "r")
text = file.readlines()
file.close()

# compile the regular expression
keyword = re.compile(r"the ")

# search file for keyword, line by line
for line in text:
  if keyword.search(line):
    print line 

# TODO: print all lines that DO NOT contain "the "
# compile the regular expression
keyword = re.compile(r"the ")

# search file for keyword, line by line
for line in text:
  if not keyword.search(line):
    print line 

# TODO: print lines that contain a word of any length starting with s and ending with e
pattern = re.compile(r'\ss\S*e\s')

# search file for keyword, line by line
for line in text:
  if pattern.search(line):
    print line 

# print dates
date = raw_input("Please enter a date in the format MM.DD.YY: ")
dates = re.compile(r'(\d\d).(\d\d).(\d\d)')
mysearch=dates.search(date)
calendar=['Month: ','Day: ','Year: ']
for i in range(1,4): print '%s%s' % (calendar[i-1],mysearch.group(i))

# TODO: Write a regular expression that finds html tags in example.html and print them.
import urllib2 
from bs4 import BeautifulSoup

web_address='http://www.andrewjclarke.net/research.html'
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read())
page = str(soup)
pattern = re.compile(r'href="(.+)"')
pattern.findall(page)

# TODO: Scrape a website and search for some things...


