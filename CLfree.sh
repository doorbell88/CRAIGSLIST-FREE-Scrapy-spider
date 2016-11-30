#!/bin/bash

# Go to directory with Craigslist Free spider
cd ~/Desktop/Programming/Python/Scrapy/CLfree

tput setaf 7
printf "\n\n\tCRAIGSLIST FREE -- MOST RECENT POSTS\n"

# wall
# ==================================================
printf "%0.s=" $( seq 1 $(tput cols) )
echo -e "\n"


# Send the spider
scrapy crawl CLfree 2>/dev/null


# wall
# ==================================================
tput setaf 7
printf "%0.s=" $( seq 1 $(tput cols) )
tput sgr0