from twython import Twython
from dateutil import parser
import datetime
import time
from datetime import datetime as dt
import pprint

API_KEY= 'sNQzHalvE4aGxVvI0YFk9LoGd'
API_SECRET= 'nthlJXIcrG34F6zBrUtBYgkjxTdUijSUbLZULMgfq6nuYtEOML'
ACCESS_TOKEN = '1454513708-RhnJUsRTXRD89HqKj5Y5I9UZDiTJI7rvCYPs565'
ACCESS_TOKEN_SECRET = 'GF89lPjYqjQXvSte4wkq3U8hKc53LojmLCm6nmDpFBHtM'

t= Twython(app_key = API_KEY,
	app_secret = API_SECRET,
	oauth_token = ACCESS_TOKEN,
	oauth_token_secret = ACCESS_TOKEN_SECRET)

def twitter1(hashtag, count):
	date1 = datetime.datetime.today()
	search = t.search(q=hashtag, count = count)
	tweets = search['statuses']
	count = 0
	i = 0
	for tweet in tweets:
		tweet_date = dt.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
		if date1.date() == tweet_date.date():
			print tweet['text']

twitter1('#PyLadies', 5)
