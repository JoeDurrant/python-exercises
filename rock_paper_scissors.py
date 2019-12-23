import random

#Generates a choice randomly if playing against the computer
def computer_choice():
    return random.randint(1,3)

#Play a game of rock, paper, scissors.
#player_number: 1 = user/CPU
#               2 = user/user
def rock_paper_scissors(player_number = 1):
    if player_number < 1 or player_number > 2:
        print("That is not a valid amount of players, enter 1 to play against the computer or 2 for multiplayer")
    else:
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        if player_number == 1:
            cpu_choice = computer_choice()
            choice = int(input("Enter your choice: "))
            if cpu_choice == choice:
                print("It's a draw - you and the computer chose the same option!")
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
        else:
            player_one_choice = int(input("Player one, enter your choice: "))
            player_two_choice = int(input("Player two, enter your choice: "))
            if player_one_choice == player_two_choice:
                print("It's a draw - you both chose the same option!")
            elif player_one_choice == 1:
                if player_two_choice == 2:
                    print("Player two wins! They chose PAPER which beats player one's ROCK")
                else:
                    print("Player one wins! They chose ROCK which beats player two's SCISSORS")
            elif player_one_choice == 2:
                if player_two_choice == 1:
                    print("Player one wins! They chose PAPER which beat player two's ROCK")
                else:
                    print("Player two wins! They chose SCISSORS which beat player one's PAPER")
            else:
                if player_two_choice == 1:
                    print("Player two wins! They chose ROCK which beat player one's SCISSORS")
                else:
                    print("Player one wins! They chose SCISSORS which beat player two's PAPER")
                
rock_paper_scissors(2)
