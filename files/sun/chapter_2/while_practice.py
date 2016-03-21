num = int(input("Enter a positive integer:"))
count = 0

print("starting with number:",num)
print("the sequence is:")

while num > 1:
    if num % 2:
        num = num*3 + 1
    else:
        num = num / 2
    print(num)
    count += 1

else:
    print()
    print("Sequence is",count,"number long")
