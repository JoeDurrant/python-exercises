import random
def cows_and_bulls():
    number = str(random.randint(1000,9999))#Generate random 4 digit number
    guessed = False
    while guessed == False:
        cow_count = 0
        bull_count = 0
        guess = input("Enter your guess (4 digit number): ")
        if guess == number:
            print("You guessed the number correctly, congratulations!")
            guessed = True
        else:
            for i in range(4):
                if guess[i] == number[i]:
                    cow_count += 1
                elif guess[i] in number:
                    bull_count += 1
            print(str(cow_count) + " cow(s), " + str(bull_count) + " bull(s)")

cows_and_bulls()
