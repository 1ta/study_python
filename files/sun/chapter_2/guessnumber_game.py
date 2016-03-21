import random
Num = random.randint(0,100)

guess = input("Guess a Number:")
guess = int(guess)

while 0 <= guess <= 100:
    if guess < Num:
        print("Guess too low, have another try!")
    elif guess > Num:
        print("Guess too big, have another try!")
    else:
        print("Lucky! You guess the right number!")
        break

    guess = input("Guess another Number:")
    guess = int(guess)

print("Sorry,you lose the game! Good luck next time!")
