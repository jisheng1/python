# 字符串转整型
from functools import reduce
import types
def str2int(str):
    def fn(x,y):
        return x * 10 + y
    def char2int(str):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[str]
    return reduce(fn,map(char2int,str))

str = '123456'
print(type(str))
num = str2int(str)
print(type(num))
