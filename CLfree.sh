#!/bin/bash

# Go to directory with Craigslist Free spider
cd ~/Desktop/Programming/Python/Scrapy/CLfree

tput setaf 7
printf "\n\n\tCRAIGSLIST FREE -- MOST RECENT POSTS\n"

# wall
# ==================================================
printf "%0.s=" $( seq 1 $(tput cols) )
echo -e "\n"




# if the first argument is empty (i.e. just type "free")
# return all results on craigslist page
if [ -z "$1" ]; then
	# Send the spider
	scrapy crawl CLfree 2>/dev/null
fi


# if you put an argument, handle it here
while [ "$1" != "" ]; do

	# if you put a number, display first (number) results
	if [[ $1 =~ ^-?[0-9]+$ ]]; then
		length=$1

		tput setaf 3
		scrapy crawl CLfree 2>/dev/null | head -n$((length * 3))
		tput sgr0
	
	# if you put a search term, display results with that term
	elif [ -n "$1" ]; then
		search_item="$1"
		tput sgr0
		# Send the spider
		scrapy crawl CLfree 2>/dev/null | grep -A1 -i "$search_item"
		echo

	fi
	shift
done



# wall
# ==================================================
tput setaf 7
printf "%0.s=" $( seq 1 $(tput cols) )
tput sgr0