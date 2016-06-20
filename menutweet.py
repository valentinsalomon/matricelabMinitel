#!/usr/bin/env python
# coding: utf-8

import os
import tweet
import search_tweet

from colorama import Fore, Back, Style

os.system('cls' if os.name == 'nt' else 'clear')

boucle = True

while boucle == True: #Infinit loop

	print (60 * '-')
	print ('\033[1m' +'La Cambuzz- Coworking')
	print ('\033[4m'+"Blablabla")
	print ('\033[0m'+'\033[3m'+'\033[2m'+"http://blabla")
	print ('\033[0m'+60 * '-')
	print ("   M A I N - M E N U")
	print (30 * '-')
	print ('\033[0m'+'\033[1m'+"1."+'\033[2m'+" Tweet @matricelab")
	print ('\033[0m'+'\033[1m' +"2. "+'\033[2m'+"Tweet")
	print ('\033[0m'+'\033[1m' +"3. "+'\033[2m'+"Quit this excellent script")
	print ('\033[0m'+30 * '-')

	is_valid=0

	while not is_valid :
		try :
		        choice = int ( raw_input('Enter your choice [1-3] : ') )
		        is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
		except ValueError, e :
		        print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])

	if choice == 1:
		print ("Starting tweet to @matricelab...")
		tweet.apicam_tweet()
	elif choice == 2:
		print ("Starting tweet...")
		tweetmsg = raw_input('Your tweet : ')
		tw = tweet.put_tweet(tweetmsg)
	#elif choice == 3:
	#	print ("Show tweets...")
	#	cron = False
	#	search_tweet.lab_tweet(cron)
	elif choice == 3:
		print('Bye bye ..\n')
		quit()
	else:
		continuer = raw_input("Invalid number. Try again...")
		os.system('cls' if os.name == 'nt' else 'clear')

quit()
