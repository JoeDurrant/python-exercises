# Basic version of hangman
def hangman():
    word = "EVAPORATE" # Hard coded word for now, all other code will adapt to this variable (length etc.)
    output_word = ["_" for i in range(len(word))] # Is a list instead of string to allow reassignment of characters
    complete = False # True if all letters have been guessed
    already_guessed = [] # Keeps track of letters which have already been guessed
    while complete == False:
        if "_" not in output_word:
            print(" ".join(output_word))
            print("Congratulations, you guessed the word!")
            complete = True # If there are no underscores in the output then the word is complete
        else:
            letter_guess = input("Guess a letter: ").upper()
            if letter_guess in word:
                if letter_guess in already_guessed:
                    print("You already guessed that letter!")
                else:
                    for i in range(len(word)):
                        if letter_guess == word[i]:
                            output_word[i] = letter_guess
                    already_guessed.append(letter_guess)
            else:
                print(letter_guess + " is not in the word, incorrect.")
        print(" ".join(output_word))
hangman()
