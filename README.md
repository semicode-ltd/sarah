# Sarah [![Build Status](https://travis-ci.org/semicode-ltd/sarah.svg?branch=master)](https://travis-ci.org/semicode-ltd/sarah)

Sarah is an English-like assistant that helps you with doing almost everything in SemiCode OS.

Sarah is your new girl friend &hearts;

She will take care of you and help you with your work. Just open a terminal anywhere you want, call her and she will be there for you.
Sarah supports a large amount of commands. They can be listed with the following command:

```bash
$ sarah list
```

Sarah uses only your username. She won't collect any personal information or send them to our servers. So we care about your privacy.

Sarah will respond to your greetings, your love or even your personal questions about her.
Just don't be rude ;)

## Some useful Sarah commands

Get movie or TV-Show information:

```bash
$ sarah watch titanic
Name : Titanic
Year of Releasing : 1997
Movie or Series : movie
Genre : Drama, Romance
Cast : Leonardo DiCaprio, Kate Winslet, Billy Zane, Kathy Bates
Ok I will watch it because it got 7.7 on imdb
```


Get the lyrics of a song:

```bash
$ sarah lyrics majerlazor leanon
<<it will output the lyrics of Major Lazors song "Lean on">>
```

Download file with resume-ability. Even if the link doesn't support resuming:

```bash
$ sarah download http://anylink.com/anyfile.tar.gz
```

Grabbing the entire content of a website for offline use:

```bash
$ sarah grab http://www.w3schools.com
```

Downloading Youtube video:

```bash
$ sarah nzli https://www.youtube.com/watch?v=7XTHdcmjenI
```

Translate any English word to Arabic word:

```bash
$ sarah translate pencil
قلم رصاص
```

Get small bio of anyone you want:

```bash
$ sarah whois Adam Levine
Adam Noah Levine (born March 18, 1979) is an American singer-songwriter, multi-instrumentalist, and actor.
He is the lead vocalist for pop rock band Maroon 5.
```

Generate "Hello World"-program in any programming language:

```bash
$ sarah first python

.py File Created Successfully , Check your Current Path
```

Get the weather of a specific city:

```bash
$ sarah weather khartoum
```

Test your internet connection speed:

```bash
$ sarah speedtest
```
Get the number of characters in any file:

```bash
$ sarah how many characters are in file.txt
34
```
Get Muslim prayer time **الأذان** (Muslim World League method)

```bash
$ sarah adhan oran Algeria
Prayer time for Algeria, Oran :
 Fajr 06:39
 Dhuhr 13:03
 Asr 15:38
 Maghrib 17:56
 Isha 19:22
```
Check the stock market : 
```bash
$ sarah marketwatch yamaha jp all
```
# Roadmap
- add autotools support

# Installation
Get all dependencies to run `Sarah` by executing:

```bash
$ sudo add-apt-repository ppa:vala-team/ppa/
$ sudo apt-get install software-properties-common
$ sudo apt-get install valac
$ sudo apt-get install libpeas-*
$ sudo apt-get install python-pip
$ sudo pip install -r requirements.txt
```
## Getting started
Swtich to your project directory and run the following commands:

```bash
$ make
$ make install
$ export LD_LIBRARY_PATH=.
$ export GI_TYPELIB_PATH=.
$ ./sarah <some command to run>
```

Enjoy your friendship with Sarah.

Made with &hearts; in Sudan.

SemiCode OS Core Team
