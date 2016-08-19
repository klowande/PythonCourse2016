# hw3, 'twit degrees of separation' klowande, 8-19-2016

import tweepy
import time

# copy/paste or import twitter-auth.py

cml = api.get_user('clairelowande') # my wife

# let most active user be the user with the most total tweets

# one degree of separation:

cml_fr = []
cml_fr_tweet_count = []
cml_fr_follower_count = []

for follower_id in cml.followers_ids():
	not_finished=True
	while not_finished:
		try:
			user = api.get_user(follower_id)
			cml_fr.append(user.screen_name)
			cml_fr_tweet_count.append(user.statuses_count)
			cml_fr_follower_count.append(user.followers_count)
			not_finished=False
		except:
			time.sleep(1)

print 'The most active friend is %s.' % cml_fr[cml_fr_tweet_count.index(max(cml_fr_tweet_count))]
print 'They have %s tweets.' % max(cml_fr_tweet_count)
print 'The most popular friend is %s.' % cml_fr[cml_fr_follower_count.index(max(cml_fr_follower_count))]
print 'They have %s followers.' % max(cml_fr_follower_count)

cml_followers = dict(zip(cml_fr, cml_fr_follower_count))

# two degrees of separation

twodeg_fr = []
twodeg_fr_tweet_count = []
twodeg_fr_follower_count = []

for follower in cml_fr:
	if cml_followers[follower] > 1000: continue # rule to ignore accts w/too many followers
	user1 = api.get_user(follower)
	for twodeg_follower in user1.followers_ids():
		not_finished=True
		while not_finished:
			try:
				user2 = api.get_user(twodeg_follower)
				if user2.followers_count > 1000: continue # rule to ignore accts w/too many followers
				twodeg_fr.append(user2.screen_name)
				twodeg_fr_tweet_count.append(user2.statuses_count)
				twodeg_fr_follower_count.append(user2.followers_count)
				not_finished=False
				print '*'
			except:
				print 'Sleeping...' # I like to see that it is doing something.
				time.sleep(1) 
				
print 'The most active friend of friends is %s.' % twodeg_fr[twodeg_fr_tweet_count.index(max(twodeg_fr_tweet_count))]
print 'They have %s tweets.' % max(twodeg_fr_tweet_count)
print 'The most popular friend of friends is %s.' % twodeg_fr[twodeg_fr_follower_count.index(max(twodeg_fr_follower_count))]
print 'They have %s followers.' % max(twodeg_fr_follower_count)

