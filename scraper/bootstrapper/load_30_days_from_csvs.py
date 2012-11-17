#! bin/ env python
import os
import csv
import sys
from database import *
import sqlalchemy

sys.path.append("..")

from stocks_scraper import *

csv_directory = "csvs"
csv_extension = '.csv'

def parse_csv(stock):

    data = csv.reader(open(csv_directory + "/" + stock + csv_extension))

    # Read the column names from the first line of the file
    fields = data.next()
    print fields
    data_list = list(data)
    total_rows = len(data_list)
    print total_rows
    first_row_to_read = total_rows - 30

    rows = []

    #print fields
    for row in data_list[-30:]:
        items = zip(fields, row)
        item = {}
        # Add the value to our dictionary
        for (name, value) in items:
            item[name] = value.strip()
        print items
        rows.append(item)
    return rows

def get_stock_id(stock):
    storage = Storage()
    storage.connect()
    stocks = meta.tables['stocks']
    query = sqlalchemy.select([stocks.c.stock_id]).where(stocks.c.symbol == stock)
    results =storage.execute(query)
    for result in results:
        print result["stock_id"]
        return result["stock_id"]


def insert_into_db(stock, rows):

    stock_id = get_stock_id(stock)
    storage = Storage()
    storage.connect()
    # stock_id date value
    daily_quotes = meta.tables['daily_quotes']
    for row in rows:
        print row
        query = sqlalchemy.insert(daily_quotes,  {"stock_id":stock_id, "date" : row["data"],  "value": row["pret inchidere"] })
        print query
        results = storage.execute(query)



if __name__ == "__main__":

    if len(argv) != 2:
        print "usage " + argv[0] + " index"
        exit(1)
    index = argv[1]

    print "Getting stocks csv_directoryist for index " + index
    stocks = scrape_stocks_by_index(index)
    print "Stocks: " + str(stocks)

    for stock in stocks:
         "Parsing CSV for stock " + stock
         rows = parse_csv(stock,)
         insert_into_db(stock, rows)
