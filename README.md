Search-Engine
=============

A small scale web search engine with reverse index and Page-rank algorithms. Have also experimented on the HITS algorithm and seeding.
Web-crawler in python that is capable of crawling pages linked from a set of a seed url’s upto a specified depth and indexing the keyword based content of the retrieved pages


--------------------
HOW TO RUN THE CODE
--------------------

This is a Python console program. The inputs that you have to provide when it asks are as follows:

Seed Page - This is the page, from which it starts crawling the web. Give the web url of a good seed page, that has ample links on it, so that it can crawl into those pages and again crawl from those pages into other pages

Search term - The term you want to search. Soon, I will add support for querying of multiple words, but for now, give a single word

eg:is algorithms

Maximum depth - This is the number of links to crawl completely. It would take 30 second for first link and for second link 60 seconds and it keeps on doubling. So, maximum 10 links are more than enough, I would say

eg:10

After you give the above three inputs, the program starts running. It may take a lot of time, to crawl depending on the depth you have specified. So the depth number, will be visible, decrementing itself, when ever a link is completely crawled; so that when it reaches 0 you know the crawling ended.

Also, I used the page rank algorithm (compute_ranks module), which is exactly what has been used in the initial days of google. The page ranks are displayed alongside the links after the search results are shown. Then the program sorts them, and presents the sorted results. For the sake of viewability, I included all these. But you can comment out the print statements in Look_up_new module to remove them.

