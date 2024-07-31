import random
print("Welcome to Rock,Paper,Scissors,Lizard,Spock game!")

while True:
    play = input("Do you wish to play? (yes/no): ")
    if play.lower() == 'yes' or play.lower() == 'no':
        break
    else:
        print("Invalid input!!! Please enter 'yes' or 'no'.")


if play.lower() == 'no':
    print("Thank you for playing Rock,Paper,Scissors,Lizard,Spock !")
    exit(1)

while True:
    type_game = input("Do you want to play against your friend or the computer? Enter 'friend' or 'computer': ")
    if type_game.lower() == 'friend' or type_game.lower() == 'computer':
        break
    else:
        print("Invalid input!!! Please enter 'friend' or 'computer'.")


while play.lower() == 'yes':
    # friend game mode
    if type_game.lower() == 'friend':
        player_1 = input("Player 1 (Rock, Paper, Lizard, Scissors, Spock): ")
        player_2 = input("Player 2 (Rock, Paper, Lizard, Scissors, Spock): ")
        if (player_1.lower() in ["rock", "paper", "lizard", "scissors", "spock"]) and (player_2.lower() in ["rock", "paper", "lizard", "scissors", "spock"]):
            condition = 1
        else:
            condition = 0

        if condition == 1:
            #tied:
            if player_1 == player_2:
                print("You tied.")

             # losing cases L
            elif player_1.lower() == "rock" and (player_2.lower() == "paper" or player_2.lower() == "spock"):
                print("Player 2 wins!")
            elif player_1.lower() == "scissors" and (player_2.lower() == "rock" or player_2.lower() == "spock"):
                print("Player 2 wins!")
            elif player_1.lower() == "paper" and (player_2.lower() == "scissors" or player_2.lower() == "lizard"):
                print("Player 2 wins!")
            elif player_1.lower() == "spock" and (player_2.lower() == "lizard" or player_2.lower() == "paper"):
                print("Player 2 wins!")
            elif player_1.lower() == "lizard" and (player_2.lower() == "scissors" or player_2.lower() == "rock"):
                print("Player 2 wins!")

            # winning cases W
            elif player_2.lower() == "rock" and (player_1.lower() == "paper" or player_1.lower() == "spock"):
                print("Player 1 wins!")
            elif player_2.lower() == "scissors" and (player_1.lower() == "rock" or player_1.lower() == "spock"):
                print("Player 1 wins!")
            elif player_2.lower() == "paper" and (player_1.lower() == "scissors" or player_1.lower() == "lizard"):
                print("Player 1 wins!")
            elif player_2.lower() == "spock" and (player_1.lower() == "lizard" or player_1.lower() == "paper"):
                print("Player 1 wins!")
            elif player_2.lower() == "lizard" and (player_1.lower() == "scissors" or player_1.lower() == "rock"):
                print("Player 1 wins!")

        elif condition == 0:
            print("The input is not correct! Try again")

    # computer game mode
    if type_game.lower() == 'computer':
        player_1 = input("Player 1 (Rock, Paper, Lizard, Scissors, Spock): ")
        computer = random.choice(['rock', 'paper', 'lizard', 'scissors', 'spock'])
        print("The computer's move: " + computer)

        if (player_1.lower() in ["rock", "paper", "lizard", "scissors", "spock"]):
            condition = 1
        else:
            condition = 0

        if condition == 1:
            # tied:
            if player_1.lower() == computer:
                print("You tied.")

            # losing cases L
            elif player_1.lower() == "rock" and (computer.lower() == "paper" or computer.lower() == "spock"):
                print("computer wins!")
            elif player_1.lower() == "scissors" and (computer.lower() == "rock" or computer.lower() == "spock"):
                print("computer wins!")
            elif player_1.lower() == "paper" and (computer.lower() == "scissors" or computer.lower() == "lizard"):
                print("computer wins!")
            elif player_1.lower() == "spock" and (computer.lower() == "lizard" or computer.lower() == "paper"):
                print("computer wins!")
            elif player_1.lower() == "lizard" and (computer.lower() == "scissors" or computer.lower() == "rock"):
                print("computer wins!")

            # winning cases W
            elif computer.lower() == "rock" and (player_1.lower() == "paper" or player_1.lower() == "spock"):
                print("Player 1 wins!")
            elif computer.lower() == "scissors" and (player_1.lower() == "rock" or player_1.lower() == "spock"):
                print("Player 1 wins!")
            elif computer.lower()== "paper" and (player_1.lower() == "scissors" or player_1.lower() == "lizard"):
                print("Player 1 wins!")
            elif computer.lower() == "spock" and (player_1.lower() == "lizard" or player_1.lower() == "paper"):
                print("Player 1 wins!")
            elif computer.lower() == "lizard" and (player_1.lower() == "scissors" or player_1.lower() == "rock"):
                print("Player 1 wins!")

        elif condition == 0:
            print("The input is not correct! Try again")

    play = input("Do you wish to play again? (yes/no): ")

    if play.lower() == 'no':
        print("Thank you for playing Rock Paper Scissors!")
        exit(1)

    type_game = input("Do you want to play against your friend or the computer? Enter 'friend' or 'computer': ")




