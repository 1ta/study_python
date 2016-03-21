theMax = int(input("Give me the upper limit:"))
sum = 0
extra = 0

for num in range(1,theMax):
    if num%2 and not num%3:
        sum += num
    else:
        extra +=  1
print(sum)
print(extra)
