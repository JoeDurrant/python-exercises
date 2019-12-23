#Play a game of rock, paper, scissors. player_number: 1 = user/CPU, 2 = user/user
def rock_paper_scissors(player_number = 1):
    if player_number < 1 or player_number > 2:
        print("That is not a valid amount of players, enter 1 to play against the computer or 2 for multiplayer")
    elif player_number == 1:
        cpu_choice = computer_choice()
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice = int(input("Enter your choice: "))
        if cpu_choice == choice:
            print("DRAW - You and the computer chose the same")
        elif choice == 1:
            if cpu_choice == 2:
                print("You lose! The computer chose PAPER which beats your ROCK")
            else:
                print("You win! The computer chose SCISSORS which was beaten by your ROCK")
        elif choice == 2:
            if cpu_choice == 1:
                print("You win! The computer chose ROCK which was beaten by your PAPER")
            else:
                print("You lose! The computer chose SCISSORS which beat your PAPER")
        else:
            if cpu_choice == 1:
                print("You lose! The computer chose ROCK which beats your SCISSORS")
            else:
                print("You win! The computer chose PAPER which was beaten by your SCISSORS")
            
import random
#Generates a choice randomly if playing against the computer
def computer_choice():
    return random.randint(1,3)
rock_paper_scissors()
