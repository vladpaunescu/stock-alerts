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
    storage.connect()
    for (stock, value) in stock_values.iteritems():
        insert_stock_quote_into_db(storage, stock, value, current_time)

    storage.disconnect()



def insert_stock_quote_into_db(storage, stock, value, current_time):
    stock_id = get_stock_id(storage, stock)

    last_value = get_last_stock_val(storage, stock_id)
    print "Last " + stock + " value:get_last_stock_val " + str(last_value)

    variaton = random.random() - 1

    new_value = float (last_value) + float(last_value) * variaton / 10

    print "New val " + str(new_value)
    realtime_quotes = meta.tables['realtime_quotes']


    query = sqlalchemy.insert(realtime_quotes,  {"stock_id":stock_id, "date_added" : current_time,  "value": new_value})
    print query
    results = storage.execute(query)

def get_not_completed_alerts(storage):
    storage.connect()
    alerts = meta.tables['alerts']
    query = sqlalchemy.select([alerts.c.id, alerts.c.value, alerts.c.stock_id, alerts.c.type, alerts.c.target_value]).where(alerts.c.date_completed == None)
    print query
    results = storage.execute(query)
    storage.disconnect()
    return results

def validate_alerts(storage, alerts):
    for item in alerts:
        print item
        stock_id = item["stock_id"]
        current_value = get_last_stock_val(storage, stock_id)
        check_if_completed(storage, current_value, item)


def check_if_completed(storage, current_val, item):
    type = item["type"]

    if type == "value":
        check_for_value(storage, current_val, item)
    else:
        check_for_percentage(storage, current_val, item)


def check_for_value(storage, current_val, item):
    target_variation = item["target_value"]
    initial_value = item["value"]

    target_alert_value = initial_value + target_variation

    if target_variation < 0 and current_val <= target_alert_value:
        mark_as_completed(storage, item)
    elif target_variation > 0 and current_val >= target_alert_value:
        mark_as_completed(storage, item)

def check_for_percentage(storage, current_val, item):
    target_variaton = item["target_value"]
    initial_value = item["value"]

    target_alert_value = initial_value + initial_value * target_variaton

    if target_variaton < 0 and current_val <= target_alert_value:
        mark_as_completed(storage, item)
    elif target_variaton > 0 and current_val >=  target_alert_value :
        mark_as_completed(storage, item)


def mark_as_completed(storage, item):
    alert_id = item["id"]
    print alert_id
    storage.connect()
    alerts = meta.tables['alerts']
    current_time = datetime.now()
    query = sqlalchemy.update(alerts).where(alerts.c.id==alert_id).values({"date_completed" : current_time } )
    print query
    results = storage.execute(query)

    storage.disconnect()


if __name__ == "__main__":

    storage = Storage()
    alerts = get_not_completed_alerts(storage)
    validate_alerts(storage, alerts)

