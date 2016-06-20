#!/usr/bin/env python
# coding: utf-8

import os
import sys
from twython import Twython, TwythonError
import random

datalovein = ["(:~ ","(:~ (:~ ","(:~ (:~ (:~ ","(:~ (:~ (:~ (:~ "]
dataloveout = ["~:) ","~:) ~:) ","~:) ~:) ~:) ","~:) ~:) ~:) ~:)"]
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

def put_tweet(x):
	os.system('cls' if os.name == 'nt' else 'clear')
	api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

	if len(x) > 140:
            print('Too many characters :/')
	else:
 	    try:
		api.update_status(status=''.join(map(str, x)))
		print('Twitter update successfull !')
	    except TwythonError as e:
		print e
	    	print('Twitter update failed : '+e)


def apicam_tweet():
	os.system('cls' if os.name == 'nt' else 'clear')
	tboucle = True
	while tboucle == True:
		print (60 * '-')
		print ('\033[1m' +"La Cambuzz "+'\033[0m'+"- Coworking")
		print ('\033[4m'+"Blablabla !") 
		print ('\033[0m'+'\033[3m'+'\033[2m'+"http://blabla")
		print ('\033[0m'+60 * '-')
		print (30 * '-')
		print ("   Tweet @Matricelab")
		print (30 * '-')
		print ("1. Send Pokoù")
		print ("2. Send Jellyfish and #Datalove")
		print ("3. Return Main Menu")
		print (30 * '-')
	
		###########################
		## Robust error handling ##
		## only accept int       ##
		###########################
		## Wait for valid input in while...not ###
		is_valid=0
		 
		while not is_valid :
			try :
				choice = int ( raw_input('Enter your choice [1-3] : ') )
				is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
			except ValueError, e :
				print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
		 
		### Take action as per selected menu-option ###
		if choice == 1:
			print ("Starting send pokoù...")
			tw = put_tweet('Hey @matricelab, '+str(random.randint(1325,1345))+' pokou ;)')
		elif choice == 2:
			# Obtenir un élément au hasard  
			i = random.randint(0, len(datalovein) - 1)  
			jellyfishin = datalovein[i]
			jellyfishout = dataloveout[i]
			print ("Starting send #Datalove...")
			tw = put_tweet('Yeapaaa, '+jellyfishin+'#Datalove'+jellyfishout+' @matricelab')
		elif choice == 3:
			print ("Okay, return...")
			os.system('cls' if os.name == 'nt' else 'clear')
			tboucle = False
		else:
			continuer = raw_input("Invalid number. Try again...")
			os.system('cls' if os.name == 'nt' else 'clear')


