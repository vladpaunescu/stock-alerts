from decimal import Decimal
import config
from stocks_scraper import *
from datetime import datetime
from db.database import  *
import random


host = config.BVB_HOST

def get_stock_values(index):
    print "Getting stocks list for index " + index
    stocks = scrape_stocks_by_index(index)
    print "Stocks: " + str(stocks)

    stock_values = {}
    for stock in stocks:
        value = scrape_stock(stock)
        print stock + ": " + value
        stock_values[stock]=value
    print stock_values
    return  stock_values

def insert_realtime_quotes_into_db(stock_values, current_time):

    storage = Storage()

    for (stock, value) in stock_values.iteritems():
        insert_stock_quote_into_db(storage, stock, value, current_time)



def insert_stock_quote_into_db(storage, stock, value, current_time):
    stock_id = get_stock_id(storage, stock)

    last_value = get_last_stock_val(storage, stock_id)
    print "Last " + stock + " value: " + str(last_value)
    print stock_id
    variaton = random.random() - 1

    new_value = float (last_value) + float(last_value) * variaton / 10

    print "New val " + str(new_value)

    storage.connect()
    realtime_quotes = meta.tables['realtime_quotes']
    query = sqlalchemy.insert(realtime_quotes,  {"stock_id":stock_id, "date_added" : current_time,  "value": new_value})
    print query
    results = storage.execute(query)
    storage.disconnect()

if __name__ == "__main__":

    index = config.INDEX
    if len(argv) == 2:
        index = argv[1]
    print "Index: " + index

    current_time = datetime.now()
    stock_values = get_stock_values(index)

    # insert into db
    insert_realtime_quotes_into_db(stock_values, current_time)

