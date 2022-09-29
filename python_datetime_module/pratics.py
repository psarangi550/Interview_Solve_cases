import datetime
import pytz #importing pytz module 
tday=datetime.datetime.today()

# print(tday.isoweekday())

#timezone aware time
# print(datetime.datetime.now(tz=pytz.UTC))
#timezone aware time
# print(datetime.datetime.utcnow().replace(tzinfo=pytz.UTC))

#converting the naive to aware datetime -- 1st approach 

# dt_aware=datetime.datetime.now(tz=pytz.UTC)

# ist_time=dt_aware.astimezone(pytz.timezone("Asia/Kolkata"))

# print(ist_time)


#converting the naive to aware datetime -- 2nd approach 

dt_naive=datetime.datetime.now() #naive datetime

tz_data=pytz.timezone("Asia/Kolkata")

dt_aware=tz_data.localize(dt_naive)

print(dt_aware)

dt_aware_us=dt_aware.astimezone(pytz.timezone("US/Mountain"))

print(dt_aware_us.isoformat())

#fetching all the timezone as below 

# for item in pytz.all_timezones:
#     print(item)