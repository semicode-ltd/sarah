#!/usr/bin/python
import sys,os,webbrowser
fc = sys.argv[1]

if (fc == "hi"):
	print("Hello "+str(os.system("whoami")))
elif (fc == "youtube"):
	url = "https://www.youtube.com/results?search_query="+sys.argv[2]
	webbrowser.open_new_tab(url)
elif (fc == "google"):
	url = "https://www.google.com/search?q="+sys.argv[2]
	webbrowser.open_new_tab(url)
elif (fc == "twitter"):
	url = "chromium-browser https://www.twitter.com/"+sys.argv[2]
	webbrowser.open_new_tab(url)
elif (fc == "time"):
	os.system("date +%Y-%m-%d::%H:%M:%S")
elif (fc == "download"):
	os.system("wget -c "+sys.argv[2])
elif (fc == "sing"):
	os.system("rhythmbox "+sys.argv[2]+".mp3")
elif (fc == "grab"):
	print("Grabbing Entire Website Content For Offline Use ...")
elif (fc == "about"):
	os.system("notify-send 'Hi , I am Sara , Your New Girlfriend <3'")
	print("My name is Sara , I am a Terminal Bot Helps You to do almost any thing in SemiCode OS , I Can Search Google and Youtube or help you to Use Twitter and Facebook For You :)")
