
while True:
    theNum = input("Please Enter an integer:")
    if not theNum.isdigit():
        print("Error:try again!")
        continue
    else:
        print(theNum)
        break
