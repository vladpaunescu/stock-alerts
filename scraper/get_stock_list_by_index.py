#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import urllib2
from sys import argv

if len(argv) != 2:
	print "usage " + argv[0] + " index"

index = argv[1]

url="http://bvb.ro/TradingAndStatistics/IndexTransactions.aspx?index=" + index

page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
stocks=soup.findAll("a", {"class": "blink1"})
for stock in stocks:
	print stock.text


