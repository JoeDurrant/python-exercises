#Guess the number game
import random

number = random.randint(1,9)

guessed = False
while guessed == False:
    user_guess = int(input("Please guess the number I'm thinking of (it's between 1 and 9): "))
    if user_guess == number:
        print("Well guessed!")
        guessed = True
    else:
        print("Nope, that guess was wrong, try again!")
