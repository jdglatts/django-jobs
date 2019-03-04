#
# Author: John Glatts
# Brief: Script to find django-jobs right from django's website.
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
				# add header
				headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
				source_code = requests.get(url, headers = headers) # pass the url to requests, HTTP for humans
				plain_text = source_code.text 
				soup = BeautifulSoup(plain_text, "html.parser") # pass/parse the url with bs4

				# playing w/ bs4 
				for jobs in soup.find_all("ul",{"class":"list-news"}):
					job_data = jobs.get_text()
					print(jobs.get_text())
					print('\n')
					writeJobs(job_data)

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


def writeJobs(job_data):
	# Write our findings to a nice txt file
	file = open("django-scrap-jobs.txt", "w", encoding="utf8")
	file.write(job_data)
	file.close()



scrapGuy()
