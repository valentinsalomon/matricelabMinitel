#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals
import sys
from twython import Twython, TwythonError
import tweet
import os

import random

datalovein = ["(:~ ","(:~ (:~ ","(:~ (:~ (:~ ","(:~ (:~ (:~ (:~ "]
dataloveout = ["~:) ","~:) ~:) ","~:) ~:) ~:) ","~:) ~:) ~:) ~:)"]
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

def lab_tweet(cron):

	fr= open('tweet.txt', 'r')
	lastTweet = fr.read()
	fr.close()
	try:
		#search_results = api.search(q='@api_cam', count=1)
		search_results = timeline_apicam().encode('utf-8')
	except TwythonError as e:
		print e

	f = open('tweet.txt', 'w')

	str2 = search_results+';@matricelab'.encode('utf-8') 
	if lastTweet == str2:
		print "nothing"
		f.write(str2)
	else:
		f.write(str2)
		response_tweet(cron)
	f.close()



def timeline_apicam():

	user_timeline = api.get_user_timeline(screen_name='matricelab')
	return user_timeline[0]['created_at']+';'+user_timeline[0]['text']

def response_tweet(cron):

	userName = "@matricelab"
	lastTL = timeline_apicam()
	fr= open('tweet.txt', 'r')
	lastTweet = fr.read()
	ltw = lastTweet.split(';',2)
	ltl = lastTL.split(';',1)
	if ltw[0] == ltl[0] and ltw[0] == ltl[0] and ltw[2] == userName:
		print 'No new tweet !'
	else:
		if "Pokou" in ltl[1]:
			tweet.put_tweet('<3 '+userName+' '+str(random.randint(1325,1345))+' Pokou :)')
		elif 'Datalove' in ltl[1]:
			# Obtenir un élément au hasard
			i = random.randint(0, len(datalovein) - 1)
			jellyfishin = datalovein[i]
			jellyfishout = dataloveout[i]
			tweet.put_tweet(jellyfishin+'#Datalove'+jellyfishout+' for you '+userName+' <3')
		else:
			tweet.put_tweet('Crazy tweet '+userName+' :D '+str(random.randint(1325,1345))+' Pokou :)')
	if cron == False:
		continuer = raw_input("See you later...")
		os.system('cls' if os.name == 'nt' else 'clear')
	fr.close()
