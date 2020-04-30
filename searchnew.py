import tweepy
from tweepy import OAuthHandler
import json
import time
import os
import datetime as dt

consumer_key = 'd4yHx0FFpgbj8R9umVIJxZjvu'
consumer_secret = 'g5fPNiPKmHBFpQiqmZ4f38aYlRSnCz2r86pwBHfU5E0H9UaGUC'
access_token = '2847125732-CdV3H3gkf6eryDsbS3ks9GP42xo8QocnHA0ZyQr'
access_secret = '6tyEN0lB9FxAhkDP6hlu4Gd0UJBxaO7CYK84L44zjSUjz'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

tweets = []
text_query = ['covid19','coronavirus','covid']
count = 100
time_limit=0.2
try:	
	for query in text_query:

		dirname=query + '/' + query
		os.makedirs(os.path.dirname(dirname), exist_ok=True)
		filename=query + '.json'
		open(filename,'a').close()
		start = dt.datetime.now()
		end = start + dt.timedelta(hours=time_limit)
		while dt.datetime.now() < end:       	
			for tweet in api.search(q=text_query, count=count):# Pulling individual tweets from query
				tweets.append((tweet.text)) 	# Adding to list that contains all tweets
			if os.path.isfile(filename):
				print('Appending tweets to file named: ',filename)
				with open(filename, 'a') as f:
					for tweet in tweets:
						json.dump(tweet, f)
						f.write('\n')	

except BaseException as e:
    print('failed on_status,',str(e))
    time.sleep(3)