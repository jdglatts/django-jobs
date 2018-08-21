# 
#
# ________________                                   ________      ______         
# ______  /_____(_)_____ ______________ ______       ______(_)________  /_________
# _  __  /_____  /_  __ `/_  __ \_  __ `/  __ \___________  /_  __ \_  __ \_  ___/
# / /_/ / ____  / / /_/ /_  / / /  /_/ // /_/ //_____/___  / / /_/ /  /_/ /(__  ) 
# \__,_/  ___  /  \__,_/ /_/ /_/_\__, / \____/       ___  /  \____//_.___//____/  
#        /___/                 /____/               /___/                     
# Script to find django- jobs. Data from django's website.
#
#


import os 
import webbrowser

import requests
from bs4 import BeautifulSoup



def scrapGuy():
	# Extract data from Drudge
		try:
			print('View Django-Jobs?')
			search = input()   
			
			if search == 'yes':
				url = 'https://www.djangoproject.com/community/jobs/' 

				# add headers
				headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
				source_code = requests.get(url, headers = headers) # pass the url to requests, HTTP for humans
				plain_text = source_code.text 
				soup = BeautifulSoup(plain_text, "html.parser") # bs4

				# find the jobs
				for jobs in soup.find_all("ul",{"class":"list-news"}):
					print(jobs.get_text())
					print('\n')

				#second check to see if we should open in browser
				print('\n Open This Search In Browser?')
				check = input()
				if check == 'yes':
					webbrowser.open(url)
				else:
					print('\n\n\n\tProgram Canceled\n\n\n')
			else:
				print('OK!')

		except  KeyboardInterrupt:
			print('\n\n\n\tProgram Canceled\n\n\n')


scrapGuy()
