# modules is a way to reuse someones code
import calendar
import math
import function#I can also write my own module,should be in the same directory otherwise use (module.name)

summation=function.sum(7,8)
print(summation)

print(math.sqrt(255))
print(dir(math))  # finding out which fucntions are avilable in math function

cal = calendar.month(2023, 9)
print(cal)
print(calendar.isleap(2023))
print(calendar.isleap(2022))



