#! bin/ env python
import csv

from db.database import *
import sqlalchemy
import  config

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


def insert_into_db(storage, stock, rows):

    storage.connect()

    stock_id = get_stock_id(storage, stock)

    # stock_id date value
    daily_quotes = meta.tables['daily_quotes']
    for row in rows:
        print row
        query = sqlalchemy.insert(daily_quotes,  {"stock_id" : stock_id, "date" : row["data"],  "value": row["pret inchidere"] })
        print query
        results = storage.execute(query)

    storage.disconnect()



if __name__ == "__main__":

    index = config.INDEX
    if len(argv) == 2:
        index = argv[1]
    print "Index: " + index

    print "Getting stocks csv_directoryist for index " + index
    stocks = scrape_stocks_by_index(index)
    print "Stocks: " + str(stocks)
    storage = Storage()

    for stock in stocks:
         "Parsing CSV for stock " + stock
         rows = parse_csv(stock)
         insert_into_db(storage, stock, rows)

