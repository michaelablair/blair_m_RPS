from gameComponents import gameVars
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def winorlose(status):
    print("You " + status + "! Would you like to " + Style.BRIGHT + "play again?")
    
    choice = input(Style.BRIGHT + Fore.GREEN + " Y " + Style.NORMAL + Fore.WHITE + "/" + Style.BRIGHT + Fore.RED + " N" + Style.NORMAL + Fore.WHITE + "? ")

    if choice == "n":
            print(Style.BRIGHT + Fore.CYAN + "~~~~~~~ Until next Time! ~~~~~~~")
            exit()

    else:
        gameVars.playerLives = 5
        gameVars.computerLives = 5
        gameVars.player = False
