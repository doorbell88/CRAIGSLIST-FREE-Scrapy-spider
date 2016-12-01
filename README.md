# CRAIGSLIST-FREE-Scrapy-spider
A spider written with Scrapy that finds the first page of newest "Craigslist Free" posts and outputs them to terminal.

    usage:  free [arguments]
                
    examples:       free 7                  -- displays the 7 newest posts
                    free table              -- displays any posts with "table" in them (letter case does not matter)
                    free table computer     -- displays any posts with "table", and then any with "computer"
                    free "computer table"   -- displays any posts with "computer table" in them
                    free 7 table            -- displays newest 7 posts, and then any with "table" in them
                

NOTE:
-----
Must have Scrapy installed for Python.  

INSTALLATION (Python)
---------------------
* With Scrapy installed, go to command line, cd to the directoy where you want this spider, and run

        $ scrapy startproject CLfree

* cd to ([Scrapy_directory]/CLfree/CLfree/spiders)

* In the spiders/ directory, add CLfree.py (from this repository)

* At this point you can cd to the directory ([Scrapy_directory]/CLfree/) and run:

        $ scrapy crawl CLfree 2>/dev/null

INSTALLATION (Shell script)
---------------------------
* Download CLfree.sh from the repository, place it in ([Scrapy_directory]/CLfree), cd to that directory, and make it executable by running:

        $ chmod 755 CLfree.sh

where ([Scrapy_directory]/CLfree/CLfree.sh) is the location of where you put CLfree.sh

Now if you type

    $ CLfree.sh

it should run the script, get rid of the extra output, and format it a little more.

If the script is not working it is likely because the directory listed in CLfree.sh is not the directory where you have put your project.

Also, make sure to make the website YOUR craigslist city and zip code URL :)


_____________________________________________________________________
For detailed instructions on starting a Scrapy project please visit:
https://doc.scrapy.org/en/latest/intro/tutorial.html
