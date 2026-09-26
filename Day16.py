#exercise
from datetime import datetime
now = datetime.now()
print(now)

date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("The format of the date is:", date)    

s_date = "5 December, 2019"
n_date = datetime.strptime(s_date, "%d %B, %Y")
print("The string date is:", n_date)

from datetime import date, datetime
t1 = date(2026, 9, 26)
t2 = date(2021, 1, 1)
print("The difference between now and new year is:", t1 - t2)

t3 = date(2026, 9, 26)
t4 = date(1970, 1, 1)
print("The difference between now and then is:", t3 - t4)




#example
from datetime import datetime
now = datetime.now()
print(now)

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
print(f'Hey, the current date & time is {hour}:{minute}, {day}/{month}/{year}.')

t = now.strftime("%H:%M:%S")
print("time:", t)

time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print("time one:", time_one)

time_c = now.strftime("%c")
print('time: ',time_c )

date = now.strftime("%x")
print(f'The date is: {date}')

date = "30 March, 2026"
dt = datetime.strptime(date, "%d %B, %Y")
print(dt)

from datetime import date as d
today = d.today()
print("Today's date:", today)

da = d(2026, 3, 30)
print("Specific date:", da)
print("Year:", da.year)

from datetime import time
t = time(12, 30, 45)
print("Time:", t)

from datetime import date, datetime
y1 = date(2026, 3, 30)
y2 = date(2026, 4, 30)
diff = y2 - y1
print("Difference between two dates:", diff.days, "days")

from datetime import timedelta
t1 = timedelta(days=5, hours=3, minutes=30)
t2 = timedelta(days=2, hours=4, minutes=15)
t3 = t1 - t2
print("Difference between two timedeltas:", t3)