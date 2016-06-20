# matricelabMinitel
## Problématique: Comment recycler un minitel en le hackant et utilisant un raspberry pi pour le faire communiquer avec un autre minitels?
Pour faire se projet nous avons dut utilisé:
- Un raspberry pi qui servira de micro ordinateur
- Un cable DIN
- Un Pl2303 qui lui, sert pour relier le DIN au raspberry
- Un minitel B1 (les B1 ont la particularité d'avoir une touche fnct "fonction" et une prise DIN femelle

C'est donc pendant un mois que j'ai eu pour mission de récupérer un minitel pour le modifier afin qu'il puisse etre utiliser comme terminale Linux. Pour commencer, j'ai passé mon temps à chercher dans sur le net des cas comparables pour trouver des tutoriels et évaluer des méthodes utilisables pour le faire dialoguer le minitel avec une carte Arduino ou un Raspberry. Etant donné que si l'on veut utiliser un mini ordinateur via SSH, avoir des applications déjà existantes et faire des “apt-get”, et pouvoir brancher un clavier, une souris et un écran, le Raspberry Pi est le meilleur choix.
Mais si l'on veut découvrir comment fonctionne une technologie, et pouvoir ajouter de nouvelles fonctions en rajoutant des modules alors le Arduino est mieux.

J'ai donc choisi le raspberry. Pour commencer à utiliser le raspberry il faut d'abbord le programmer en installant Raspbian, en faite Raspbian est un système d'exploitation libre et gratuit fondé sur GNU/Linux/Debian et optimisé pour fonctionner sur un Raspberry Pi. Ensuite après avoir installer Raspbian, nous l'avons branché à la télévision du cambuzz et nous l'avons paramétré (langues,mot de passe).
Nous avons fait un bot twitter sur un raspberry pi, se qui va nous donner des informations sur la température du CPU, combien de temps est-il allumé. Pour cela il faut installer les paquets suivants:

'''
sudo apt-get install python-setuptools python-dev libffi-dev libssl-dev python-pip
sudo pip install twython
sudo pip install requests[security]
'''

Puis il faut se connecter sur l'Application Management de Twitter, avec le compte bot
pour y générer un token et ensuite le remplacer dans les différents scripts python (4 en tout).

Sources:
http://wiki.labomedia.org/index.php/Renaissance_d%27un_Minitel_avec_une_Raspberry_Pi
http://wiki.labomedia.org/index.php/Conversation_avec_un_minitel
http://blog.uggy.org/?post/2015/02/22/Minitel-et-Raspberry
http://wiki.labomedia.org/images/9/91/Minitel_1_bistandard_alcatel.pdf
http://pila.fr/wordpress/?p=425
http://xseignard.github.io/2013/05/20/plug-your-minitel-on-your-raspberry-pi/
http://tonyisageek.blogspot.fr/p/telic-alcatel-minitel-running-as-usb.html
http://www.virtualabs.fr/Super-Minitel-Entertainment-System
http://hxc2001.free.fr/minitel/Presentation_Etude_Minitel_2_FR_DE.pdf
http://hxc2001.free.fr/minitel/

RaspPi
http://fr.rs-online.com/web/generalDisplay.html?id=raspberrypi
http://www.framboise314.fr/raspberry-pi-3-quoi-de-neuf-docteur/
http://branchez-vous.com/2016/02/29/le-raspberry-pi-3-passage-64-bits-pour-le-pc-miniature-35-us/

Twitter
https://angristan.fr/faire-un-bot-twitter-sur-son-raspberry-pi/
https://github.com/Angristan/AngristanRPiBot

Commandes Linux 
http://lea-linux.org/documentations/Shell

Question reponse Twitter
http://naelshiab.com/quand-twitter-rencontre-python/
http://socialmedia-class.org/twittertutorial.html
http://naelshiab.com/tutoriel-vos-premiers-pas-en-python/
https://github.com/twitterdev/sample-python-autoreply
https://github.com/bear/python-twitter
https://blog.twitter.com/2014/getting-started-with-automation-on-twitter
http://www.dototot.com/reply-tweets-python-tweepy-twitter-bot/
