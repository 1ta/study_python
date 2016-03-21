print("Allow the user to enter a series of integers. Sum the integers")
print("Ignore non-numeric input. End input with'.' ")

theSum = 0

while True:
    theNum = input("Number:")
    if theNum == '.':
        break
    if not theNum.isdigit():
        print("Error,only numbers please")
        continue
    theSum += int(theNum)

print("The Sum is:", theSum)
