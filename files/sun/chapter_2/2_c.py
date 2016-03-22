Sum = 0
Max = int(input("please Enter a integer:"))

for num in range(1, Max+1):
    Sum = Sum + num
    if Sum % num == 0:
        print (Sum)
