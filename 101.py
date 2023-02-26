from persiantools.jdatetime import JalaliDate, JalaliDateTime
import datetime
import pytz

# date = str(JalaliDateTime(1401, 12, 6, 20, 1, 10, 0, pytz.utc).strftime("%c"))
# day = date.split()
# print(day[0])

date = str(JalaliDateTime(1401, 12, 6, 20, 1, 10, 0, pytz.utc).strftime("%A"))
print(date)
