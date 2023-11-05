import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
print(x.strftime("%w"))
print(x.strftime("%B"))
print(x.strftime("%Y"))

import platform

x = platform.system()


x = dir(platform)

print(x)

import module1 as mx

mx.greeting("David")

age = mx.person["age"]
print(age)

from module1 import person

print(person["country"])