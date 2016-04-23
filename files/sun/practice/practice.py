def multiply(a,b):
    return a*b
def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def divise(a,b):
    return a*1.0/b
ops = {
    '*': multiply,
    '+': plus,
    '-': minus,
    '/': divise
}

def operate(a,op,b):
    return ops[op](a,b)

print(operate(8,'+',8) == 12)
print(operate(10,'-',3) == 7)
print(operate(3,'*',3) == 6)
print(operate(8,'/',2)== 4)
