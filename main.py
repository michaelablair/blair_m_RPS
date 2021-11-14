from random import randint
from gameComponents import winLose, gameVars, gameRules
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


print(Fore.CYAN + Style.BRIGHT + "~~~~~~~ Game On! ~~~~~~~")

while gameVars.player is False:

    gameVars.player = input(Style.BRIGHT + "Choose your weapon:" + Fore.WHITE + " rock, paper, or scissors: ")
    gameVars.computer = gameVars.choices[randint(0, 2)]


    print(Style.DIM + "-----" + Fore.WHITE + Style.NORMAL + " Player attacks with  " + Style.BRIGHT + gameVars.player + "! " + Style.DIM + "-----")
    print(Style.DIM + "-----" + Fore.WHITE + Style.NORMAL + " Computer attacks with " + Style.BRIGHT + gameVars.computer + "! " + Style.DIM + "-----")

    gameRules.winner()

    print("Computer lives: " + str(gameVars.computerLives))
    print ("Your lives: " + str(gameVars.playerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("have been " + Fore.RED + "defeated" + Fore.WHITE)

    elif gameVars.computerLives == 0:
        winLose.winorlose("are " + Fore.GREEN + "victorious" + Fore.WHITE)

    gameVars.player = False

