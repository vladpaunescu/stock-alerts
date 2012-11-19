from __future__ import division
import sqlalchemy
import  config
from realtime_scraper_mock import insert_realtime_quotes_into_db

connection_string = 'mysql://%s:%s@%s/%s?charset=utf8&use_unicode=0' % (
config.USER, config.PASSWORD, config.HOST, config.DB)
engine = sqlalchemy.create_engine(connection_string, pool_recycle=3600, pool_size=5, max_overflow=10)
meta = sqlalchemy.MetaData()
meta.reflect(bind=engine)

class Storage(object):
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = engine.connect()

    def disconnect(self):
        try:
            self.conn.close()
            self.conn = None
        except Exception, e:
            print e

    def execute(self, query):
        try:
            result = self.conn.execute(query)
            return result
        except Exception, e:
            print e


def get_stock_id(storage, stock):
    storage.connect()
    stocks = meta.tables['stocks']
    query = sqlalchemy.select([stocks.c.stock_id]).where(stocks.c.symbol == stock)
    results =storage.execute(query)
    storage.disconnect()
    for result in results:
        print result["stock_id"]
        return result["stock_id"]

def get_last_stock_val(storage, stock_id):
    storage.connect()
    realtime_quotes = meta.tables['realtime_quotes']
    query = sqlalchemy.select([realtime_quotes.c.value]).where(realtime_quotes.c.stock_id == stock_id).order_by(realtime_quotes.c.date_added.desc())
    print query
    results = storage.execute(query)
    storage.disconnect()

    for result in results:
        return result["value"]

if __name__ == "__main__":

    storage = Storage()

    stocks = meta.tables['stocks']
    query = sqlalchemy.select([stocks.c.stock_id, stocks.c.symbol, stocks.c.name])
    results =storage.execute(query)
    for result in results:
        print result["symbol"]
        get_stock_id(storage, result["symbol"])
    storage.disconnect()

