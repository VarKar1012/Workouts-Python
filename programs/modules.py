# time module
import time

# print(time.time()) #1696919157.4400277
# print(time.localtime(time.time())) #time.struct_time(tm_year=2023, 
#     # tm_mon=10, tm_mday=10, tm_hour=11, tm_min=55, tm_sec=57, 
#     # tm_wday=1 (represent tuesday(starts from monday as 0)), 
#     # tm_yday=283, tm_isdst=0)

# print(time.asctime()) #Tue Oct 10 11:59:08 2023

# print(dir(time)) #to get all the fns in the module
# print(help(time)) #to get all the fns in the module in doc format

# t1 = (2023, 9, 20, 12, 0, 0, 0, 0, 0)
# print(time.mktime(t1))
# print(time.localtime(time.mktime(t1)))

# time.sleep(3)#time in sec
# # s/m waits for 3 min
# ---------------------------------------------------------------------

import timeit # to know exec time of code portion
# print(timeit.timeit('[i*2 for i in range(100)]'))

# ---------------------------------------------------------------------

import calendar #calender info

# print(calendar.calendar(2024)) #outputs calender of the year 2024

# print(calendar.isleap(2020)) True

# print(f"Leap days between 1995 and 2023:", calendar.leapdays(1995, 2023)) #Leap days between 1995 and 2023: 7

# print(dir(calendar))

# print(calendar.month(2023, 10, 4, 1)) #4(length), 1(width)

# print(calendar.weekday(2023,10,10))

# print(calendar.MONDAY)

# ---------------------------------------------------------------------

import datetime

# print(datetime.date(2023, 10, 10)) #2023-10-10
# print(datetime.date.today()) #2023-10-10

# dt = datetime.date(2023, 10, 10)
# print(dt.year)
# print(dt.month) #10
# print(dt.day) #12
# print(dt.weekday()) # 1 - tuesday
# print(dt.isoweekday()) # 2 - tuesday; monday has value 1 and onwards

# print(datetime.date.ctime(datetime.date(2023, 10, 10))) #Tue Oct 10 00:00:00 2023

# dt = datetime.date.today()
# td = datetime.timedelta(days=3)
# print(dt + td) #2023-10-13
# print(dt - td) #2023-10-07

# ---------------------------------------------------------------------

import random

# print(random.random()) # prints random nums b/w 0 - 1 in float
# print(random.uniform(1, 5)) # random nums b/w  1-5 in float

# print(random.randint(1, 10)) # returns integer b/w 1 - 10

# print(random.randrange(10)) # returns random value from given range

# val = ['red', 'abc', 'green', 'black']
# choices() - returns a list, choice()-returns a value/string

# print(random.choices(val)) # returns list of single value
# print(random.choices(val, k=2)) #['red', 'abc'] - returns list of 2 values
# print(random.choices(val, weights=[10, 10, 15, 20], k=2)) # weights-setting priority
# highest priority values will be paired together in the first few iterations : ['black', 'black']

# v = random.choice(val)
# print(v, 'fruit') #abc fruit, green fruit
# print(random.choice(['varna', 'pranav', 'hari'])) # returns a value from given list

# l = list(range(1,21))
# random.shuffle(l)
# print(l) #[2, 14, 9, 1, 4, 8, 3, 10, 11, 5, 16, 7, 13, 18, 15, 6, 19, 12, 20, 17]

# print(random.sample(l, k=5)) #[1, 2, 5, 3, 10] returns 5 random values from the list

# ---------------------------------------------------------------------

# any / all / abs / round / min / max functions
# print(any([1])) #checks if any of the value is not empty str / not 0/ not False
# print(any([1, 0, 3])) #true
# print(any([True, False, True]))#true
# print(any([False])) #false
# print(any(['', 'a'])) #true
# print(any(['', ''])) #false

# print(all(['abc', 12, 1])) #true - checks if all the values in iterable 
                            # is not empty str / not 0 / not False
# print(all(['abc', 12, 1, False])) #false
# print(all(['', 12, 1])) #false
# print(all([12, 1])) #true
# print(all([12, 1, True])) #true

# print(abs(-11)) #11
# print(abs(-11.4)) #11.4

# print(round(11.5)) #12
# print(round(11.54556, 2)) #11.55
# print(round(113, 2)) #113

# print(min([2,3,4]))#2
# print(max([2,3,4]))#4

# ---------------------------------------------------------------------

import math

# print(dir(math))
# print(math.sqrt(5)) #2.23
# print(math.factorial(5)) #120
# print(math.pi) #3.141592653589793
# print(math.sin(180)) #-.8
# print(math.cos(90)) #-0.448

# print(math.ceil(5.6)) #6 - converts the number to nearest higest integer
# print(math.ceil(5.6)) #6
# print(math.ceil(5.2)) #6

# print(math.floor(5.6)) #5 - converts the number to nearest lower integer
# print(math.floor(5.4)) #5
# print(math.floor(5)) #5

# print(math.trunc(5.66)) #5 - converts the number to its integer part
# print(math.trunc(5)) #5
# print(math.trunc(5.4)) #5

# ---------------------------------------------------------------------

import statistics as s
# from statistics import *

# print(dir(statistics))
# print(mean([1,2,3,4,5])) #3

# print(s.median([1,2,3,4,5])) #3
# print(median([1,2,3,4,5, 6])) #3.5
# print(median([3,4,1,2,5, 6])) #3.5 - returns middle value of a list in fraction

# print(mode([1,2,3,4,5, 3])) #3 - returns first occuring duplicated value
# print(multimode([1,2,3,4,5, 3, 1])) #[1, 3] - returns all duplicated values

# ---------------------------------------------------------------------







