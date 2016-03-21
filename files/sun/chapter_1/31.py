import math

a = 3
b = 7
c = 9

cosC = float((a**2+b**2-c**2)/(2*a*b))
cosA = float((c**2+b**2-a**2)/(2*c*b))
cosB = float((c**2+a**2-b**2)/(2*a*c))

A = math.acos(cosA)/math.pi*180
B = math.acos(cosB)/math.pi*180
C = math.acos(cosC)/math.pi*180

print(A,B,C)
