
def digui(n):
    if n == 1:
        return 1
    return n * digui(n-1)

def digui2(n):
    num = 1
    for i in range(1,n+1):
        num = num * i
    return num

print (digui(5))
print (digui2(4))
