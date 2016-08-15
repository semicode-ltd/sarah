#!/usr/bin/python
import sys,os,webbrowser,getpass,urllib
from bs4 import BeautifulSoup
fc = sys.argv[1]
if (fc == "hi"):
	print("Hello "+getpass.getuser())
elif (fc == "youtube"):
	url = "https://www.youtube.com/results?search_query="+sys.argv[2]
	webbrowser.open_new_tab(url)
elif (fc == "google"):
	url = "https://www.google.com/search?q="+sys.argv[2]
	webbrowser.open_new_tab(url)
elif (fc == "twitter"):
	url = "chromium-browser https://www.twitter.com/"+sys.argv[2]
	webbrowser.open_new_tab(url)
elif (fc == "sc"):
	url = "https://soundcloud.com/search?q="+sys.argv[2]
	webbrowser.open_new_tab(url)
elif (fc == "lyrics"):
	url = "http://www.azlyrics.com/lyrics/"+sys.argv[2]+"/"+sys.argv[3]+".html"
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	# kill all script and style elements
	for script in soup(["script", "style"]):
		script.extract()    # rip it out

	# get text
	text = soup.get_text()

	# break into lines and remove leading and trailing space on each
	lines = (line.strip() for line in text.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# drop blank lines
	text = '\n'.join(chunk for chunk in chunks if chunk)

	print(text)
elif (fc == "time"):
	os.system("date +%Y-%m-%d**%H:%M:%S")
elif (fc == "download"):
	os.system("wget -c "+sys.argv[2])
elif (fc == "grab"):
	print("Grabbing Entire Website Content For Offline Use ...")
elif (fc == "nzli"):
	os.system("youtube-dl "+sys.argv[2])
elif (fc == "about"):
	os.system("notify-send 'Hi , I am Sara , Your New Girlfriend <3'")
	print("Hi , I am Sara , Your New Girlfriend <3 ")
elif (fc == "help"):
	print("* Available Commands For Sara : \n 1- hi \n 2- youtube \n 3- google \n 4- twitter \n 5- time \n 6- download \n 7- grab \n 8- about \n 9- sc ")
