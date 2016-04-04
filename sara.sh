#!/bin/bash
if [ "$1" = "h*" ]
then
echo "Hello $USER :)"
fi
if [ "$1" = "time" ]
then
date +%Y-%m-%d::%H:%M:%S
fi
if [ "$1" = "about" ]
then
echo "Sara is a Terminal Bot Help You to do almost any thing in the SemiCode OS , You Can Search Google and Youtube Use Twitter and Facebook "
fi
if [ "$1" = "google" ]
then
chromium-browser https://www.google.com/search?q=$2
fi
if [ "$1" = "howdoi" ]
then
howdoi $*
fi
if [ "$1" = "youtube" ]
then
chromium-browser https://www.youtube.com/results?search_query=$2
fi
