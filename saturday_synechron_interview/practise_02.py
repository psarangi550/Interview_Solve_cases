import datetime
import pytz
#first Approach
dt_aware=datetime.datetime.now(tz=pytz.UTC)
print(dt_aware.astimezone(pytz.timezone('Asia/Kolkata')))
#second Approach
dt_naive=datetime.datetime.now()
ist_time=pytz.timezone('Asia/Kolkata')
print(ist_time.localize(dt_naive))

# for tz in pytz.all_timezones:
#     print(tz)