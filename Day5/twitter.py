#Register an app: https://dev.twitter.com/

#sudo pip install tweepy
import tweepy
import time

#Check the documentation page
#http://docs.tweepy.org/en/v3.2.0/

# copy/paste or import twitter-auth.py


#See rate limit
api.rate_limit_status()

#Create user objects
ksl = api.get_user('ksl_')
krugman = api.get_user('NYTimeskrugman')
ksl = api.get_user('Klowande')

#What can I do using this object?
dir(ksl)

#Get some information
ksl.id
ksl.name
ksl.screen_name
ksl.location
ksl.profile_location

dave=api.get_user('jabbersoccer')
dave.profile_image_url

#Check her tweets
ksl.status
ksl.status.text
ksl.statuses_count
dave.statuses_count

#Check her followers
ksl.followers_count
ksl.followers() #creates a list of user objects - only the first 20!
type(ksl.followers()[0])
ksl.followers()[0].screen_name #the results are user result sets as well
api.followers(ksl.id,count=200) #creates a list of user objects - can get up to 200

ksl.followers_ids() #creates a list of user ids - up to 5000
api.followers_ids('ksl_')

for follower_id in ksl.followers_ids():
	user = api.get_user(follower_id)
	print user.screen_name

#How to deal with limits

#Get the first 2 "pages" of follower ids
krugmans_followers=[]

for page in tweepy.Cursor(api.followers_ids, 'NYTimeskrugman').pages(2):
    krugmans_followers.extend(page) #extend is like extend, but can take arguments with length greater than 1
    time.sleep(60) # not good practice, no guarantee you hit your limit.
    
#Get the ids of 6000 followers
krugmans_followers=[]

for item in tweepy.Cursor(api.followers_ids, 'NYTimeskrugman').items(6000):
	print item
	krugmans_followers.append(item)
	time.sleep(api.rate_limit_status('remaining'))
	
###If you are running code, this time.sleep will not gaurantee you don't go over the limit.
# Exercise: write generic code that will never break (this will be very helpful for everything you do, including the homework)

## this doesn't work - but see tweet dumper code
theDonalds_followers=[]
for item in tweepy.Cursor(api.followers_ids, 'realDonaldTrump').items(10000):
	while len(item) > 0:
		print item
		theDonalds_followers.append(item)


