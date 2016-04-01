import math
nums = input("Enter 4 numbers(split with common):")
l=[]
for i in nums.split(","):
    l.append(int(i))


def multiply(a,b):
    return a*b
def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def divise(a,b):
    return a*1.0/b
op = {
    '*': multiply,
    '+': plus,
    '-': minus,
    '/': divise
}

ops = ['*','+','-','/']
