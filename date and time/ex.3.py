"""
Exercise 2: Convert string into a datetime object
For example, You received the following date in string format. 
Please convert it into Python’s DateTime object.

"""

from datetime import datetime
str1= "Feb 25 2020  4:20PM"

date_obj= datetime.strptime(str1, '%b %d %Y %I:%M%p')
print(date_obj)

# from datetime import datetime

# date_string = "Feb 25 2020  4:20PM"
# datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
# print(datetime_object)
