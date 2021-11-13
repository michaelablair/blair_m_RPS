from random import randint
from gameComponents import winLose, gameVars


while gameVars.player is False:
    
    gameVars.player = input("Choose your weapon: rock, paper, or scissors: ")
    gameVars.computer = gameVars.choices[randint(0, 2)]

    print("player chose: " + gameVars.player)
    print("computer chose: " + gameVars.computer)

    if gameVars.computer == gameVars.player:
        print("tie! try again")

    elif gameVars.player == "rock":
        if gameVars.computer == "paper":
            print("you lose!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("you win!")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "paper":
        if gameVars.computer == "scissors":
            print("you lose!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("you win!")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "scissors":
        if gameVars.computer == "rock":
            print("you lose!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("you win!")
            gameVars.computerLives = gameVars.computerLives - 1

    print("computer lives: " + str(gameVars.computerLives))
    print ("player lives: " + str(gameVars.playerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("lost")

    elif gameVars.computerLives == 0:
        winLose.winorlose("won")

    gameVars.player = False

