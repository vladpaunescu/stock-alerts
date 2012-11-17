#! bin/ env python
import os

import sys
sys.path.append("..")

from stocks_scraper import *

host ="http://www.kmarket.ro/"
csv_directory = "csvs"

def get_csv(stock):
    extension =".csv"

    url =  host + "/inc/istoric.php?simbol=" + stock
    page=urllib2.urlopen(url)
    localFile = open(csv_directory + "/" + stock + ".csv",'w')
    localFile.write(page.read())
    page.close()
    localFile.close()

def ensure_dir(f):
    script_dir = os.path.dirname(sys.argv[0])
    d = os.path.dirname(script_dir + "/" + f)
    if not os.path.exists(d):
        os.makedirs(d)

if __name__ == "__main__":
    if len(argv) != 2:
        print "usage " + argv[0] + " index"
        exit(1)

    index = argv[1]
    print "Getting stocks csv_directoryist for index " + index
    stocks = scrape_stocks_by_index(index)
    print "Stocks: " + str(stocks)

    ensure_dir(csv_directory)

    for stock in stocks:
        print "Downloading CSV for stock" + stock
        get_csv(stock)

