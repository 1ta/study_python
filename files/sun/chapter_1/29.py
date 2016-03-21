import math

X = float(input("Type the weight of Mr Jones:"))

r = 6.378*10**6
m1 = 5.9742*10**24
G = 6.67300*10**-11

F = int(m1*X*G/r**2)
g = F/X

print(F,g)
