#!/usr/bin/env python
# coding: utf-8

import search_tweet
import time

boucle = True

while boucle == True: #Infinit loop

	cron = True
	search_tweet.lab_tweet(cron)
	time.sleep(30)
