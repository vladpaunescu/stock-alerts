#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import urllib2
from sys import argv

host="http://bvb.ro"


def scrape_stocks_by_index(index):
	url = host + "/TradingAndStatistics/IndexTransactions.aspx?index=" + index
	page=urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	stocks=soup.findAll("a", {"class": "blink1"})
	return [el.text for el in stocks[1:]] # skipping feedback anchor link	

def scrape_stock(stock_symbol):
	url="http://bvb.ro/ListedCompanies/SecurityDetail.aspx?s=" + stock_symbol
	page=urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	stocks=soup.findAll("span", {"id": "ctl00_central_lbPrice"})
	if stocks is not None:
		return stocks[0].text
	return -1
	
if __name__ == "__main__":
	if len(argv) != 2:
		print "usage " + argv[0] + " index"
		exit(1)

	index = argv[1]
	print "Getting stocks list for index " + index
	stocks = scrape_stocks_by_index(index)
	print "Stocks: " + str(stocks)
	
	stock_values = {}	
	for stock in stocks:
		value = scrape_stock(stock)
		print stock + ": " + value
		stock_values[stock]=value
	
	print stock_values

