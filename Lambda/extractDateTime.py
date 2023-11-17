# Sample Output:
# 2020-01-15 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178

# date = "2020-01-15 09:03:32.744178"

# date_split = date.split()
# year_extrt = lambda x: x.split('-')

# print("year:\n", '\n'.join(year_extrt(date_split[0])))
# print("time:\n", date_split[1])

# --------------------------------------------------------

import datetime

current = datetime.datetime.now()
# print(current.time())

year = lambda x: x.year
print("year:", year(current))

month = lambda x: x.month
print("month:", month(current))

date = lambda x: x.day
print("date:", date(current))

time = lambda x: x.time()
print("time:", time(current))