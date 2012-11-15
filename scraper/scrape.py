#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import urllib2

url="http://bvb.ro/ListedCompanies/SecurityDetail.aspx?s=FP"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
stocks=soup.findAll("span", {"id": "ctl00_central_lbPrice"})
for stock in stocks:
	print stock.text
