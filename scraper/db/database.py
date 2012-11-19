from __future__ import division
import sqlalchemy
import  config
from realtime_scraper_mock import insert_realtime_quotes_into_db

connection_string = 'mysql://%s:%s@%s/%s?charset=utf8&use_unicode=0' % (
config.USER, config.PASSWORD, config.HOST, config.DB)
engine = sqlalchemy.create_engine(connection_string, pool_recycle=3600, pool_size=5, max_overflow=10)
meta = sqlalchemy.MetaData()
meta.reflect(bind=engine)

### DB ###
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

#def get_total_unique_visitors_query(f, t):
#    users = meta.tables['omniture_app_users']
#    query = sqlalchemy.select([users.c.application, users.c.date,
#                               users.c.value, users.c.daily_value],
#        from_obj=users).where(sqlalchemy.and_(users.c.metric == 'First Launch', users.c.date >= f, users.c.date <= t)).order_by(users.c.date)
#    return query
#
#def get_total_first_launches_query(from_date, to_date):
#    users = meta.tables['omniture_app_users']
#    query = sqlalchemy.select([users.c.application, sqlalchemy.func.ifnull(sqlalchemy.func.sum(users.c.daily_value),0).label('total_first_launches')],
#        from_obj=users).where(sqlalchemy.and_(users.c.metric == "First Launch", users.c.date>=from_date, users.c.date<=to_date)).group_by(users.c.application)
#    return query
#
#def get_opt_ins(f, t):
#    users = meta.tables['omniture_app_users']
#    query = sqlalchemy.select([users.c.application, users.c.date,
#                               users.c.value, users.c.metric],
#        from_obj=users).where(sqlalchemy.and_(sqlalchemy.or_(users.c.metric == 'opt-in', users.c.metric == 'opt-out', users.c.metric == 'opt-in-change', users.c.metric == 'opt-out-change'), users.c.date >= f, users.c.date <= t)).order_by(users.c.date)
#    return query
#
#def get_monthly_unique_visitors_query(f, t):
#    users = meta.tables['omniture_app_users']
#    query = sqlalchemy.select([users.c.application, users.c.date, users.c.monthly_value],
#        from_obj=users).where(sqlalchemy.and_(users.c.metric == 'Launch', users.c.date >= f, users.c.date <= t)).order_by(users.c.date)
#    return query
#
#def get_cloud_costs_query(f, t, backend='CC'):
#    costs = meta.tables['cloud_costs']
#    query = sqlalchemy.select([
#        sqlalchemy.func.sum(costs.c.ec2).label("ec2"),
#        sqlalchemy.func.sum(costs.c.sdb).label("sdb"),
#        sqlalchemy.func.sum(costs.c.sns).label("sns"),
#        sqlalchemy.func.sum(costs.c.s3).label("s3"),
#        sqlalchemy.func.sum(costs.c.cloudfront).label("cloudfront"),
#        sqlalchemy.func.sum(costs.c.sqs).label("sqs"),
#        sqlalchemy.func.sum(costs.c.route53).label("route53"),
#        sqlalchemy.func.sum(costs.c.emr).label("emr"),
#        sqlalchemy.func.sum(costs.c.rds).label("rds"),
#        sqlalchemy.func.sum(costs.c.vpc).label("vpc"),
#        sqlalchemy.func.sum(costs.c.transfer).label("transfer")],
#        from_obj=costs).where(sqlalchemy.and_(costs.c.backend==backend, costs.c.date >= f,
#        costs.c.date <= t)).order_by(costs.c.date)
#    return query
#
#
#'''
#@see http://dev.mysql.com/doc/refman/4.1/en/example-maximum-column-group-row.html
#select b.application, b.date, b.value from
#    (select application, max(date) as max_date from omniture_app_users where date <='2011-08-09' and metric = 'opt-in-rate' group by application) as a
#    inner join omniture_app_users as b on a.application=b.application and a.max_date = b.date and metric='opt-in-rate'
#'''
#def get_optin_rates_query(date):
#    table = meta.tables['omniture_app_users']
#    inner_query=sqlalchemy.select([table.c.application, sqlalchemy.func.max(table.c.date).label("max_date")], from_obj=table).where(sqlalchemy.and_(table.c.date<=date, table.c.metric=="opt-in-rate")).group_by(table.c.application)
#    left = inner_query.alias("left")
#    right = table.alias("right")
#    join = left.join(right, onclause=sqlalchemy.and_(left.c.application==right.c.application, left.c.max_date == right.c.date, right.c.metric == 'opt-in-rate'))
#    query = sqlalchemy.select([join.right.c.application, join.right.c.date, join.right.c.value], from_obj = join)
#    return query
#
#def get_ratings(f,t):
#    ratings = meta.tables['store_ratings']
#    query = sqlalchemy.select([ratings.c.application, ratings.c.date,
#                               sqlalchemy.func.sum(ratings.c.num_rating_5).label("num_rating_5"),
#                               sqlalchemy.func.sum(ratings.c.num_rating_4).label("num_rating_4"),
#                               sqlalchemy.func.sum(ratings.c.num_rating_3).label("num_rating_3"),
#                               sqlalchemy.func.sum(ratings.c.num_rating_2).label("num_rating_2"),
#                               sqlalchemy.func.sum(ratings.c.num_rating_1).label("num_rating_1")],
#        from_obj=ratings).group_by(ratings.c.application,ratings.c.date).where(sqlalchemy.and_(ratings.c.date >= f,
#        ratings.c.date <= t)).order_by(ratings.c.date)
#    print query
#    return query
#
#
#SEGMENTS_TO_REPORT = {
#    ("date", "parent")          : "actions",
#    ("date", "store")           : "actions",
#    ("date", "parent", "store") : "actions",
#    ("country",)                : "countries"
#}
#
##get CC downloads&revenues grouped by various dimensions (e.g "application", "store", "store,app", "device", "platform")
#def get_downloads_and_revenues(f, t, storage, segments):
#    # infer report table name from segments requested
#    report_table = SEGMENTS_TO_REPORT.get(segments, None)
#    if not report_table:
#        raise Exception("Cannot find report table for segments: %s" % str(segments))
#    print "Report table selected", report_table
#    table = meta.tables[report_table]
#    group = [getattr(table.c, x) for x in segments]
#    projection = list(group)
#    projection.extend([sqlalchemy.func.sum(table.c.units).label("downloads"),
#                       sqlalchemy.func.sum(table.c.proceeds).label("revenue")])
#    where_clause = [table.c.date >=f, table.c.date <= t]
#    if report_table == "actions": #dirty hack, we need to filter out updates
#        where_clause.append(table.c.action != 'update')
#
#    query = sqlalchemy.select(projection, from_obj = table)\
#    .where(sqlalchemy.and_(* where_clause))\
#    .group_by(*group)\
#    .order_by(table.c.date)
#    results = storage.execute(query)
#    return [dict(result.items()) for result in results]
#
#def get_devices(f, t):
#    devices = meta.tables["devices"]
#    query = sqlalchemy.select([devices.c.device, sqlalchemy.func.sum(devices.c.units).label("downloads")], from_obj=devices).where(sqlalchemy.and_(
#        devices.c.date >= f, devices.c.date <= t)).group_by(devices.c.device).order_by(devices.c.date)
#    return query
#
#def get_platforms(f, t):
#    platforms = meta.tables["platforms"]
#    query = sqlalchemy.select([platforms.c.platform, sqlalchemy.func.sum(platforms.c.units).label("downloads")], from_obj=platforms).where(sqlalchemy.and_(
#        platforms.c.date >= f, platforms.c.date <= t)).group_by(platforms.c.platform).order_by(platforms.c.date)
#    return query
#
#def get_global_average_rating():
#    ratings = meta.tables['store_ratings']
#    query = sqlalchemy.select([ratings.c.application,
#                               sqlalchemy.func.sum(ratings.c.num_rating_5).label("num_rating_5"),
#                               sqlalchemy.func.sum(ratings.c.num_rating_4).label("num_rating_4"),
#                               sqlalchemy.func.sum(ratings.c.num_rating_3).label("num_rating_3"),
#                               sqlalchemy.func.sum(ratings.c.num_rating_2).label("num_rating_2"),
#                               sqlalchemy.func.sum(ratings.c.num_rating_1).label("num_rating_1")],
#        from_obj=ratings).group_by(ratings.c.application).order_by(ratings.c.date)
#    print query
#    return query
#
#def get_total_revenues():
#    actions = meta.tables['actions']
#    query = sqlalchemy.select([
#        sqlalchemy.func.sum(actions.c.proceeds).label("proceeds")],
#        from_obj=actions)
#    return query
#
#def get_range_revenues(from_date, to_date):
#    actions = meta.tables['actions']
#    where_clause = [actions.c.date >= from_date, actions.c.date <= to_date]
#    query = sqlalchemy.select([
#        sqlalchemy.func.sum(actions.c.proceeds).label("proceeds")],
#        from_obj=actions).where(sqlalchemy.and_(* where_clause))
#    return query
#
## get data from saasbase
#def get_ims_active_users(from_date, to_date):
#    return hbase_call("/clients/acc/ims/reports.json", "ims__stats", from_date, to_date, "year+month+day+app+active_users", {}, ['year', 'month', 'day', 'app'], "", 0, 1)
#
#def get_ims_unique_users(from_date, to_date):
#    return hbase_call("/clients/acc/ims/reports.json", "ims__stats", from_date, to_date, "year+month+day+app+uniques", {}, ['year', 'month', 'day', 'app'], "", 0, 1)
#
#def get_apps_per_users(to_date):
#    return hbase_call("/clients/acc/ims/reports.json", "ims__stats", to_date, to_date, "year+month+day+apps_number", {}, ['apps_number'], "", 0, 0)
#
#def get_apps_combination_per_users(to_date):
#    return hbase_call("/clients/acc/ims/reports.json", "ims__stats", to_date, to_date, "year+month+day+apps_combination", {}, ['apps_combination'], "", 0, 0)
#
#### VIEWS ###
#def downloads_view(results,segments):
#    data = []
#    for result in results:
#        if 'parent' in segments:
#            result['parent'] = get_app_short_name(result['parent'])
#            if not result['parent']: #unknown app, skip it
#                continue
#        dimensionLabel = "/".join([result[segment] for segment in segments if segment != 'date'])
#        downloads = int(result["downloads"])
#        revenue = round(float(result["revenue"]),2) if result["revenue"] else 0
#        result_dict = {
#            "name": unicode(dimensionLabel).encode('utf-8'),
#            "downloads": downloads,
#            "revenue": revenue,
#            "revenue_per_download": round(revenue / downloads,2) if downloads else 0
#        }
#        if "date" in segments:
#            result_dict["date"] = result["date"].strftime("%Y-%m-%d")
#
#        data.append(result_dict)
#    return json.dumps(data)
#
#def error_view(exception):
#    return json.dumps({"status": "error", "message": str(exception)})
#
#'''
#Params:
#    results     :  the unique visitors dataset from omniture
#    optin_rates :  dictionary of opt-in rates  at the requested date for each app
#'''
#def total_unique_visitors_view(results, optin_rates):
#    data = []
#    for result in results:
#        #skip unknown apps
#        app = get_app_short_name(result["application"])
#        if not app:
#            continue
#            #raw data from omniture
#        visitors = int(result["value"]) if result["value"] else 0
#        first_launches = int(result["daily_value"]) if result["daily_value"] else 0
#        #normalize data according to opt-in rate
#        optin_rate = optin_rates.get(result['application'],None)
#        if optin_rate:
#            visitors *= 1.0/optin_rate
#            first_launches *= 1.0/optin_rate
#        data.append({
#            "name": app,
#            "visitors": visitors,
#            "first_launches": first_launches,
#            "date": result["date"].strftime("%Y-%m-%d")
#        })
#    return json.dumps(data)
#
#def monthly_unique_visitors_view(results, optin_rates):
#    data = []
#    for result in results:
#        app = get_app_short_name(result["application"])
#        if not app: continue
#        #raw data from omniture
#        monthly_uniques = int(result["monthly_value"]) if result["monthly_value"] else 0
#        #normalize data according to opt-in rate
#        optin_rate = optin_rates.get(result['application'],None)
#        if optin_rate:
#            monthly_uniques*= 1.0/optin_rate
#        data.append({
#            "name": get_dimension_short_name(result["application"]),
#            "monthly_unique": monthly_uniques,
#            "date": result["date"].strftime("%Y-%m-%d")
#        })
#    return json.dumps(data)
#
#def retention_rate_view(active_users, first_launches, optin_rates):
#    data = []
#    total_first_launches = {}
#    for result in first_launches:
#        #raw data from omniture
#        total_first_launches[result['application']] = int(result['total_first_launches'])
#        total_launches = int(result['total_first_launches'])
#        #normalize data according to opt-in rate
#        optin_rate = optin_rates.get(result['application'],None)
#        if optin_rate:
#            total_launches*= 1.0/optin_rate
#        total_first_launches[result['application']] = total_launches
#
#    for result in active_users:
#        app = get_app_short_name(result["application"])
#        if not app: continue
#        #raw data from omniture
#        monthly_value = int(result["monthly_value"]) if result["monthly_value"] else 0
#        #normalize data according to opt-in rate
#        optin_rate = optin_rates.get(result['application'],None)
#        if optin_rate > 0:
#            monthly_value*= 1.0/optin_rate
#        data.append({
#            "name": app,
#            "retention_rate": monthly_value / (total_first_launches[result['application']] if total_first_launches.has_key(result['application']) else 1),
#            "date": result["date"].strftime("%Y-%m-%d")
#        })
#    return json.dumps(data)
#
#def opt_ins_view(results):
#    partial_data = {}
#    data = []
#
#    for result in results:
#        date = result["date"].strftime("%Y-%m-%d")
#        app = get_app_short_name(result["application"])
#        if not app: continue
#        if not partial_data.has_key(date):
#            partial_data[date] = {}
#        if not partial_data[date].has_key(app) :
#            partial_data[date][app] = {}
#        partial_data[date][app].update({result["metric"]:int(result["value"]) if result["value"] else 0})
#
#    for date in partial_data:
#        for app in partial_data[date]:
#            part = {"name": app, "date": date}
#            part.update(partial_data[date][app])
#            data.append(part)
#    for d in data:
#        optIn = (int(d["opt-in"]) if d.has_key("opt-in") else 0)
#        optOut = (int(d["opt-out"]) if d.has_key("opt-out") else 0)
#        optInChange = (int(d["opt-in-change"]) if d.has_key("opt-in-change") else 0)
#        optOutChange = (int(d["opt-out-change"]) if d.has_key("opt-out-change") else 0)
#
#        newOptIn = optIn + optOutChange - optInChange
#        newOptOut = optOut + optInChange - optOutChange
#        d["opt-in"] = newOptIn if newOptIn > 0 else 0
#        d["opt-out"] = newOptOut if newOptOut > 0 else 0
#
#        if d.has_key("opt-in-change"):
#            del d["opt-in-change"]
#        if d.has_key("opt-out-change"):
#            del d["opt-out-change"]
#    return json.dumps(data)
#
#def cloud_costs_view(results):
#    data = []
#    for result in results:
#        for k in result.keys():
#            print "%s, %s" % (k , type(result[k]))
#            if (result[k]):
#                data.append({
#                    "name": k,
#                    "cost": result[k]
#                })
#    return json.dumps(data)
#
#def ratings_view(results):
#    data = []
#    for result in results:
#        ratings_sum = 0
#        ratings_count = 0
#        for i in range(1,6):
#            r = result["num_rating_%d" % i]
#            ratings_sum += i*r
#            ratings_count += r
#        avg_rating = round(ratings_sum / ratings_count, 2)
#        if result["application"] in mappings.acc_apps:
#            display_name = mappings.acc_apps[result["application"]].display_name
#        else:
#            display_name = result["application"]
#        data.append({
#            "name": display_name,
#            "date": result["date"].strftime("%Y-%m-%d"),
#            "avg_rating": avg_rating
#        })
#    return json.dumps(data)
#
#def global_ratings_view(results):
#    data = []
#    for result in results:
#        ratings_sum = 0
#        ratings_count = 0
#        for i in range(1, 6):
#            r = result["num_rating_%d" % i]
#            ratings_sum += i*r
#            ratings_count += r
#        avg_rating = round(ratings_sum / ratings_count, 2)
#        data.append({
#            "name": mappings.acc_apps[result["application"]].display_name,
#            "avg_rating": avg_rating
#        })
#    return json.dumps(data)
#
#def devices_view(results):
#    data = []
#    for result in results:
#        data.append({
#            "name": result["device"],
#            "downloads": int(result["downloads"])
#        })
#    return json.dumps(data)
#
#def platforms_view(results):
#    data = []
#    for result in results:
#        data.append({
#            "name": result["platform"],
#            "downloads": int(result["downloads"])
#        })
#    return json.dumps(data)
#
#def ims_active_users_view(results):
#    data = []
#    for result in results:
#        data.append({
#            "name": result["app"],
#            "users": int(result["users"]),
#            "date": '%(year)04d-%(month)02d-%(day)02d' % {"year": int(result["year"]), "month" : int(result["month"]) , "day" : int(result["day"])}
#        })
#
#    return json.dumps(data)
#
#def ims_unique_users_view(results):
#    data = []
#    for result in results:
#        data.append({
#            "name": result["app"],
#            "users": int(result["users"]),
#            "date": '%(year)04d-%(month)02d-%(day)02d' % {"year": int(result["year"]), "month" : int(result["month"]) , "day" : int(result["day"])}
#        })
#
#    return json.dumps(data)
#
#def apps_per_users_view(results):
#    data = []
#    for result in results:
#        data.append({
#            "number": int(result["apps_number"].encode('hex'), 16),
#            "users": int(result["users"])
#        })
#
#    return json.dumps(data)
#
#def apps_combination_per_users_view(results):
#    data = []
#    for result in results:
#        data.append({
#            "number": int(result["apps_combination"].encode('hex'), 16),
#            "users": int(result["users"])
#        })
#
#    return json.dumps(data)
#
#'''
#returns the revenues data
#'''
#def home_total_revenues_view(results):
#    revenue = 0
#    for result in results:
#        if result["proceeds"] != None:
#            revenue += int(result["proceeds"])
#    return revenue
#
#def get_app_short_name(app):
#    #query for app_id
#    apps = mappings.get_acc_apps(app_id=app)
#    if apps:
#        return apps[0].display_name
#        #query for sku (i.e. sku or alias)
#    apps = mappings.get_acc_apps(sku=app)
#    if apps:
#        return apps[0].display_name
#        #give up
#    print "Unknown app: %s" % str(app)
#    return None
#get_stock_id

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

