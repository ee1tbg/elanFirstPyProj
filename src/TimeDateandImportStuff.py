'''
Created on Sep 3, 2018

@author: Winterberger
'''
#import datetime
from datetime import datetime

current_time = datetime.now()
later_time = datetime.now()

month = current_time.month
minute = current_time.minute
second = current_time.second
ms = current_time.microsecond

print (type(current_time))
print (current_time)
print (later_time)
print (second)

print ("%02d-%02d-%04d" % (current_time.month, current_time.day, current_time.year))
print ("%02d/%02d/%04d" % (current_time.month, current_time.day, current_time.year))
print ("%02d:%02d:%02d" % (current_time.hour, current_time.minute, current_time.second))

print ("%02d/%02d/%04d %02d:%02d:%02d" % 
       (current_time.month, current_time.day, current_time.year, current_time.hour, current_time.minute, current_time.second))