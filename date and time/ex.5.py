"""
Exercise 4: Print a date in a the following format
Day_name  Day_number  Month_name  Year

"""
from datetime import datetime

date= datetime(2004, 4, 20)
print("give dayte is:-")
print(date.strftime('%A %D %B %Y'))