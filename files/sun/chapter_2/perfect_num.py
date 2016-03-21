Num = input("Enter a number to check:")
Num = int(Num)
divisor = 1
Sumofdivisor = 0
while Num > divisor:
    if Num % divisor == 0:
        Sumofdivisor = Sumofdivisor + divisor
    divisor = divisor + 1 # consist with while or will cycle forever

if Num == Sumofdivisor:
    print(Num,"is a perfect Numbber")
else:
    print(Num,"is not a perfect Number")
