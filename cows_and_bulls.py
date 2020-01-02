import random
def cows_and_bulls():
    number = str(random.randint(1000,9999))
    guessed = False
    while guessed == False:
        cow_count = 0
        bull_count = 0
        guess = input("Enter your guess: ")
        if len(guess) != 4 or not guess.isdigit():
            print("Your guess has to be a 4 digit number!")
        elif guess == number:
            print("Congratulations! You guessed the number!")
            guessed = True
        else:
            already_guessed = [] # Track which digits have already been checked, stops cows being recounted when counting bulls
            # Check cow and bull count
            for i in range(4):
                if guess[i] == number[i]:
                    cow_count += 1
                    already_guessed.append(guess[i]) # Fixes bull count
                elif guess[i] != number[i] and guess[i] not in already_guessed and guess[i] in number:
                    already_guessed.append(guess[i])
                    bull_count += 1
            print(str(cow_count) + " cow(s), " + str(bull_count) + " bull(s)")

cows_and_bulls()