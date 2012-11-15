#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import urllib2

url="http://bvb.ro/TradingAndStatistics/IndexTransactions.aspx?index=BET"

page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
stocks=soup.findAll("a", {"class": "blink1"})
for stock in stocks:
	print stock.text
