from random import randint

# add player and computer lives
playerLives = 5
computerLives = 5

# save the player as a varable called player
# the value of player will be one of three choices to type (inpput)
player = input("Choose rock, paper, or scissors: ")

print("player chose: " + player)

# an array is a container. it holds multiple values in a 0-based index
# you can store anything in an array
# and retrieve it later. Arrays have square bracket notation

choices = ["rock", "paper", "scissors"]

computer = choices[randint(0, 2)]

print("computer chose: " + computer)

if (computer == player):
    print("tie! try again")

elif (player == "rock"):
    if (computer == "paper"):
        print("you lose!")
        playerLives = playerLives - 1
    else:
        print("you win!")
        computerLives = computerLives - 1

elif (player == "paper"):
    if (computer == "scissors"):
        print("you lose!")
        playerLives = playerLives - 1
    else:
        print("you win!")
        computerLives = computerLives - 1

elif (player == "scissors"):
    if (computer == "rock"):
        print("you lose!")
        playerLives = playerLives - 1
    else:
        print("you win!")
        computerLives = computerLives - 1

print("computer lives: " + str(computerLives))
print ("player lives: " + str(playerLives))

