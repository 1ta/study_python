import math

radiusInteger = int(input("Enter the radius of your circle: "))

circumference = 2 * math.pi * radiusInteger
area = math.pi * (radiusInteger ** 2)

print("The circumference is :",circumference,",and the area is:",area)
