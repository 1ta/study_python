GUESS_COUNT = 5

import random
Num = random.randint(0,100)
count_left = GUESS_COUNT

while count_left > 0:
    if count_left == GUESS_COUNT:
        print("Guess a Number!You have",count_left,"chances!")
    else:
        print("Guess another Number!You have",count_left,"chances!")
    guess = input()
    guess = int(guess)
    if guess > 100 or guess < 0:
        break
    if guess < Num:
        print("Guess too low!")
    elif guess > Num:
        print("Guess too big!")
    else:
        print("Lucky! You guess the right number!")
        break
    count_left = count_left - 1

if count_left == 0:
    print("Sorry,you lose the game! Good luck next time!")
else:
    print("Sorry,you leave the game! Good luck next time!")
