import random

number=int(random.randrange(1,10))
turns=3
Guess=0

while turns>0:
    print("turns remaining: " + str(turns))
    userInput = input("guess a number between 1 and 10: ")
    if userInput.isdigit():
        guess=int(userInput)
    else:
        guess=0
        print("invalid guess")
        continue

    if guess>0 and guess<10:
        if guess==number:
            print("you guessed the number! congrats")
            break
        elif guess>number:
            print("your guess is too high")
            turns -=1
        elif guess<number:
            print("your guess is too low")
            turns -=1
        else:
            print("invalid number")

if turns == 0:
    print("you ran out of turns,better luck next time")

