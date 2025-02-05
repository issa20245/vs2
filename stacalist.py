import math
import random as r
def log(*arg):
    for i in arg:
        print(arg)
value = []
def store(val):
    value.append(val)
def sqrt(opr):
     return math.sqrt(opr)
def big(*num):
    for i in range(1):
        print(max(num))
def small(*num):
    for i in range(1):
        print(min(num))
def rand(a,b):
    return print(r.randint(a,b))
def grf(h,w):
    for i in range(h):
        print(w)
def ask(val):
    return input(val)