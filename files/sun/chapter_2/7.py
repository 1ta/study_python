a = 0
b = 0
c = 0
d = 0
for i in range(1,10):
    a = a * 10 + i
    print(a, '*', 8, '+', i, '=', a*8+i)

for i in range(1,10):
    b = b * 10 + i
    print(b,'*',9,'+',i+1,'=',b*9+i+1)

for i in range(0,7):
    c = c * 10 + 9 - i
    print(c,'*',9,'+',7-i,'=',c*9+7-i)

for i in range(0,10) :
    d = 10**i + d
    print(d,'*',d,'=',d**2)
