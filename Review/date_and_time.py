import time
from datetime import datetime, date, timedelta
from time import strftime, strptime, gmtime, mktime, sleep
from dateutil.relativedelta import relativedelta
print(date.today())
print(datetime.now().time())

date_string = "Feb 25 2020 4:20PM"
print(datetime.strptime(date_string, "%b %d %Y %I:%M%p"))


given_date = datetime(2020, 2, 25)
print(given_date - timedelta(7))

print(given_date.strftime("%A %d %B %Y"))
given_date = datetime(2020, 7, 26)
print(given_date.strftime("%A"))

given_date = datetime(2020, 3, 22, 10, 0, 0)

print(given_date + timedelta(days=7, hours=12))

print(datetime.time(datetime.now()))
print(time.time())

given_date = datetime(2020, 2, 25)
print(given_date.strftime("%Y-%m-%d %H:%M:%S"))


given_date = datetime(2020, 2, 25).date()
print(given_date.replace(month=6))

new_date = given_date + relativedelta(months=+4)
print(new_date)


date_1 = datetime(2020, 2, 25)
date_2 = datetime(2020, 9, 17)
print(date_2 - date_1)