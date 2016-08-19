# For the purposes of this exercise, we define three types of Twitter users. 
# Layman: Users with less than 100 followers
# Expert: Users with 100-1000 followers
# Celebrity: Users with more than 1000 followers

# Two degrees of separation: For the following two questions, limit your search of
# followers and friends to laymen and experts.
# Among the followers of your target and their followers, who is the most active? 
# Among the friends of your target and their friends, who is the most active?

# hw3, 'twit degrees of separation' klowande, 8-19-2016

import tweepy
import time

# copy/paste or import twitter-auth.py

cml = api.get_user('clairelowande')

# Most active user = total tweets

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

twodeg_fr = []
twodeg_fr_tweet_count = []
twodeg_fr_follower_count = []

for follower in cml_fr:
	if cml_followers[follower] > 1000: continue
	user1 = api.get_user(follower)
	for twodeg_follower in user1.followers_ids():
		not_finished=True
		while not_finished:
			try:
				user2 = api.get_user(twodeg_follower)
				if user2.followers_count > 1000: continue
				twodeg_fr.append(user2.screen_name)
				twodeg_fr_tweet_count.append(user2.statuses_count)
				twodeg_fr_follower_count.append(user2.followers_count)
				not_finished=False
				print '*'
			except:
				print 'Sleeping...'
				time.sleep(1)