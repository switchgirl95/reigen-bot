import tweepy
import time
import os
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)

auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit =True, wait_on_rate_limit_notify=True)

user = api.me()

search = '#reigen'
nrTweets = 10

for tweet in tweepy.Cursor(api.search, q="#reigen OR #reigenredraw OR #redrawreigen OR #reigenarataka OR #aratakareigen OR #100daysofMobPsycho -nsfw -mpreg -#reitome -#mobrei -#mobreigen -#mobxreigen -#reimob -#indiefilm -#indiegame -#100DaysofCode").items():
#for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
	try:
		#print('Tweet Liked')
		tweet.retweet()
		time.sleep(900)
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break
