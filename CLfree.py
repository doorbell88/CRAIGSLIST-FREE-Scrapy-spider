# Craigslist Free spider

"""
Searches craigslist free section in my city and zip code
outputs top 5 (newest) results

--> You will need to change the URL in the class definition
to reflect your own city/zip
"""

import scrapy
import os

number_of_listings = 5


class FreeSpider(scrapy.Spider):
    name = "CLfree"
    start_urls = [
        'http://boulder.craigslist.org/search/zip?query=80304',
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
            print listing.css('a::attr(href)').extract()[0]
            print

            if i >= number_of_listings:
                os.system('tput sgr0')
                exit()


