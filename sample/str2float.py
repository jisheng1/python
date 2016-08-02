# -*- coding: utf-8 -*-
# 字符串转浮点型
from functools import reduce
import types
def str2float(s):
    intger = s.split('.')[0]
    decimal = s.split('.')[1]
    def str2num(str):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[str]
    def fn(x,y):
        return x * 10 + y
    def fn1(x,y):
        return float(x) / 10 + y

    intger = reduce(fn,map(str2num,intger))
    
    decimal = map(str2num,decimal)
    decimal.reverse()
    decimal = reduce(fn1,decimal) / float(10)
    
    return intger + decimal

print(str2float('123.456'))    
print(type(str2float('123.456')))
