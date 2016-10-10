#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys,os,webbrowser,getpass,urllib,io
from bs4 import BeautifulSoup
from translate import Translator
from imdbpie import Imdb
fc = sys.argv[1]
panum = len(sys.argv)
if (fc == "hi"):
	print("Hello "+getpass.getuser())
elif (fc == "i"):
	if (sys.argv[2] == "love"):
		print("I Love You Too "+getpass.getuser())
elif (fc == "good"):
	if (sys.argv[2] == "morning"):
		print(fc +" "+sys.argv[2]+" "+getpass.getuser())
	else:
		print(fc +" "+sys.argv[2]+" "+getpass.getuser())
elif (fc == "youtube"):
	que = ""
	for i in range(2,len(sys.argv)):
		que = que +" "+sys.argv[i]
	url = "https://www.youtube.com/results?search_query="+que
	webbrowser.open_new_tab(url)
elif (fc == "google"):
	que = ""
	for i in range(2,len(sys.argv)):
		que = que +" "+sys.argv[i]
	url = "https://www.google.com/search?q="+que
	webbrowser.open_new_tab(url)
elif (fc == "github"):
	que = ""
	for i in range(2,len(sys.argv)):
		que = que +" "+sys.argv[i]
	url = "https://github.com/search?utf8=✓&q="+que
	webbrowser.open_new_tab(url)
elif (fc == "twitter"):
	que = ""
	for i in range(2,len(sys.argv)):
		que = que +" "+sys.argv[i]
	url = "https://www.twitter.com/"+que
	webbrowser.open_new_tab(url)
elif (fc == "sc"):
	que = ""
	for i in range(2,len(sys.argv)):
		que = que +" "+sys.argv[i]
	url = "https://soundcloud.com/search?q="+que
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
	que = ""
	for i in range(2,len(sys.argv)):
		que = que +" "+sys.argv[i]
	os.system("youtube-dl "+que)
elif (fc == "translate"):
	translator= Translator(to_lang="ar")
	translation = translator.translate(sys.argv[2])
	print(translation)
elif (fc == "about"):
	os.system("notify-send 'Hi , I am Sarah , Your New Girlfriend <3'")
	print("Hi , I am Sarah , Your New Girlfriend <3 ")
elif (fc == "imdb"):
	imdb = Imdb()
	title = imdb.get_title_by_id(sys.argv[2])
	print(title.title)
	print(title.rating)
elif (fc == "first"):
	if (sys.argv[2] == "python"):
		with io.FileIO("first.py", "w") as file:
			file.write("print(\"Hello World!\")")
    			print(".py File Created Successfully , Check your Current Path")
	elif(sys.argv[2] == "java"):
		with io.FileIO("first.java", "w") as file:
			file.write("public class first {\npublic static void main (String []args){\nSystem.out.println(\"Hello World!\");\n}")
    			print(".java File Created Successfully , Check your Current Path")
	elif(sys.argv[2] == "bash"):
		with io.FileIO("first.sh", "w") as file:
			file.write("#!/bin/sh\necho \"Hello World\"")
    			print(".sh File Created Successfully , Check your Current Path")
	elif(sys.argv[2] == "c"):
		with io.FileIO("first.c", "w") as file:
			file.write("#include <stdio.h>\nint main(void){\nprintf(\"Hello, world\");\n}")
    			print(".c File Created Successfully , Check your Current Path")
	elif(sys.argv[2] == "html"):
		with io.FileIO("first.html", "w") as file:
			file.write("<html><head><title>My First Page</title></head><body>Hello World</body></html>")
    			print(".html File Created Successfully , Check your Current Path")
	elif(sys.argv[2] == "php"):
		with io.FileIO("first.php", "w") as file:
			file.write("<?php echo \"Hello World !!\"?>")
			os.system("sudo mv /home/$USERNAME/Project_stuffs/Sarah/first.php /var/www/html/first.php");
    			print(".php File Created Successfully , Navigate to http://localhost/first.php to See The Result")
	elif(sys.argv[2] == "c#"):
		with io.FileIO("first.cs", "w") as file:
			file.write("class First {\n static void main () {\nSystem.Console.Write(\"Hello World\");\n}")
    			print(".cs File Created Successfully , Check your Current Path")
elif (fc == "run"):
	os.system(sys.argv[2])
elif (fc == "weather"):
	if len(sys.argv) < 3:
		print("Usage : sara weather city \n ex: sara weather khartoum")
	else:
		os.system("curl wttr.in/"+sys.argv[2])
elif (fc == "speedtest"):
	os.system("speedtest")
elif (fc =="koora"):
	os.system("soccer --live") 
elif (fc == "passive"):
	os.system("watch -n 900 \"notify-send -t 3000 'Look away. Rest your eyes'\"")
elif (fc == "how"):
	if (sys.argv[2] == "many"):
		if (sys.argv[3] == "characters"):
			if (sys.argv[4] == "are"):
				if (sys.argv[5] == "in"):
					utf8_text=open(sys.argv[6],'r+').read()
					unicode_data = utf8_text.decode('utf8')
					print len(unicode_data)
elif (fc == "web"):
	if (sys.argv[2] == "wordpress"):
		print("Downloading Latest Version of Wordpress ...")
		os.system("wget https://wordpress.org/latest.zip")
		print("Extracting Zip Files ...")
		os.system("unzip latest.zip")
		print("Zip File Extracted Successfully")
		pname = input_raw("Enter Project Name : ")
		print("Moving Wordpress to /var/www/html/"+pname)
		os.system("sudo cp -R latest /var/www/html/"+pname)
		os.system("sudo chmod -R 777 /var/html/"+pname)
		sqlname = input_raw("Enter MySQL Username : ")
		sqlpass = input_raw("Enter MySQL Password : ")
		db1 = MySQLdb.connect(host="localhost",user=sqlname,passwd=sqlpass)
		cursor = db1.cursor()
		sql = 'CREATE DATABASE word'
		cursor.execute(sql)
		print("Database Created Successfully ")
		print("Editing Configuration File ")
		
		
elif (fc == "help"):
	print("* Available Commands For Sarah : \n 1- hi \n 2- youtube \n 3- google \n 4- twitter \n 5- time \n 6- download \n 7- grab \n 8- about \n 9- sc \n 10- nzli (to download youtube videos) \n 11- imdb \n 12- translate \n 13- speedtest \n 14- first \n")
else :
	print("Sorry I don't Know What you mean By ("+sys.argv[1]+") , Write sara help to list Available Commands")
