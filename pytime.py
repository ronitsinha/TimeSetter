from datetime import datetime
from calendar import monthrange
import win32api
import urllib.request
from bs4 import BeautifulSoup
import ctypes, sys


now = datetime.now ()

# Getting time from just-the-time
try:
	req = urllib.request.Request('http://just-the-time.appspot.com/', headers={'User-Agent' : 'Magic Browser'})
	web_page = urllib.request.urlopen(req).read()

	data = str(web_page).replace ('b', '').replace("'", '')

	date = data.split(' ') [0]
	day = int (date.split ('-') [2])
	month = int (date.split ('-') [1])
	year = int (date.split ('-') [0])
	weekday = datetime(year, month, day).weekday()

	time = data.split(' ') [1]
	hour = int (time.split (':') [0])
	minute = int (time.split (':') [1])
	second = int (time.split (':') [2])

	win32api.SetSystemTime (year, month, weekday, day, hour, minute, second, 10)	

	print (data)	
except Exception as e:
	raise e


# Getting time from Time.is
# try:
# 	req = urllib.request.Request("https://time.is", headers={'User-Agent' : "Magic Browser"}) 
# 	web_page = urllib.request.urlopen(req).read()

# 	amORpm = ''

# 	soup = BeautifulSoup(web_page, "html.parser")
# 	twd = soup.find ("div", {"id" : "twd"})


# 	colonSplit = twd.text.split (':');

# 	if colonSplit[2] != colonSplit [2].replace ('PM', ''):
# 		amORpm = 'PM'
# 	elif colonSplit[2] != colonSplit[2].replace ('AM', ''):
# 		amORpm = 'AM'

# 	'''
# 	0 - hour
# 	1 - minute
# 	2 - second
# 	amORpm - morning or evening
# 	'''

# 	time = [int (colonSplit [0]), int (colonSplit [1]), int (colonSplit [2].replace ('PM', '').replace ('AM', ''))]

# 	year = now.year
# 	month = now.month
# 	weekday = datetime.today().weekday()
# 	day = now.day

# 	# Convert to 24 hour time
# 	if amORpm == 'PM':
# 		time[0] += 12

# 	if time[0] + 4 <= 24:
# 		time[0] += 4
# 	else:
# 		time[0] = (time[0] + 4) - 24
# 		day += 1		
# 		weekday += 1
# 	if weekday > 7:
# 		weekday -= 7

# 	if day > monthrange (year, month) [1]:
# 		day -= monthrange (year, month) [1]
# 		month += 1
# 	if month > 12:
# 		month -= 12
# 		year += 1

# 	print ('Time.is time ' + str (time [0]))
# 	print ('System time: ' + str (now.hour))

# 	#TODO: set the calendar date too

# 	#win32api.SetSystemTime (year, month, weekday, day, time[0], time[1], time[2], 10)

# except Exception as e:
# 	raise e
