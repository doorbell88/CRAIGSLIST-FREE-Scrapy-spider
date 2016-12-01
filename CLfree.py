# Craigslist Free spider

"""
Searches craigslist free section in my city and zip code
outputs top 5 (newest) results

--> You will need to change the URL in the class definition
to reflect your own city/zip
"""

import scrapy
import os

# If you want to limit the results displayed...
# number_of_listings = 10


class FreeSpider(scrapy.Spider):
    name = "CLfree"
    start_urls = [
        # 'http://boulder.craigslist.org/search/zip?query=80304',
        'http://boulder.craigslist.org/search/zip?search_distance=25&postal=80304',
    ]



    def parse(self, response):
        i=0

        for listing in response.css('div.content ul.rows li.result-row'):


            # Next listing:
            i += 1

            # TITLE
            print "  (%s)\t" %(i),
            os.system('tput setaf 3')
            print listing.css('p.result-info a::text').extract_first()
            os.system('tput sgr0')

            # LINK
            print "\t",
            os.system('tput setaf 6')
            link_suffix = listing.css('a::attr(href)').extract()[0]
            # if link_suffix[1] != "/":
            #     print link_suffix[1:]
            # else
            #     print "http://boulder.craigslist.org"+link_suffix
            print "http://boulder.craigslist.org"+link_suffix
            print

            # if i >= number_of_listings:
            #     os.system('tput sgr0')
            #     exit()


