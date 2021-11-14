from random import randint
from gameComponents import winLose,gameVars
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def winner():
    if gameVars.computer == gameVars.player:
        print(Style.BRIGHT + Back.YELLOW + "You both miss. Try again!")

    elif gameVars.player == "rock":
        if gameVars.computer == "paper":
            print(Style.BRIGHT + Back.RED + "Computer lands a hit! You take damage.")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print(Style.BRIGHT + Back.GREEN + "You land a hit! Computer takes damage.")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "paper":
        if gameVars.computer == "scissors":
            print(Style.BRIGHT + Back.RED + "Computer lands a hit!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print(Style.BRIGHT + Back.GREEN + "You land a hit! Computer takes damage.")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "scissors":
        if gameVars.computer == "rock":
            print(Style.BRIGHT + Back.RED + "Computer lands a hit!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print(Style.BRIGHT + Back.GREEN + "You land a hit! Computer takes damage.")
            gameVars.computerLives = gameVars.computerLives - 1