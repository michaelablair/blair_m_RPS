from random import randint

choices = ["rock", "paper", "scissors"]

# player will be the weapon chosen via input
# Boolean values are True or False - you can use these to check state
# and make programming choices based on their value
player = False

# lives need to decrement upon losing a round
playerLives = 5
computerLives = 5

while player is False:

    player = input("Choose your weapon: rock, paper, or scissors: ")
    computer = choices[randint(0, 2)]

    print("player chose: " + player)
    print("computer chose: " + computer)

    if computer == player:
        print("tie! try again")

    elif player == "rock":
        if computer == "paper":
            print("you lose!")
            playerLives = playerLives - 1
        else:
            print("you win!")
            computerLives = computerLives - 1

    elif player == "paper":
        if computer == "scissors":
            print("you lose!")
            playerLives = playerLives - 1
        else:
            print("you win!")
            computerLives = computerLives - 1

    elif player == "scissors":
        if computer == "rock":
            print("you lose!")
            playerLives = playerLives - 1
        else:
            print("you win!")
            computerLives = computerLives - 1

    print("computer lives: " + str(computerLives))
    print ("player lives: " + str(playerLives))

    if playerLives == 0:
        print("you lost! would you like to play again?")
        choice = input(" Y / N? ")

        if choice == "n":
            print("better luck next time!")
            exit()

        else:
            playerLives = 5
            computerLives = 5
            player = False

    elif computerLives == 0:
        print("you won! would you like to play again?")
        choice = input(" Y / N? ")

        if choice == "n":
            print("better luck next time!")
            exit()

        else:
            playerLives = 5
            computerLives = 5
            player = False


    player = False

