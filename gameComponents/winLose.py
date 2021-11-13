from gameComponents import gameVars

def winorlose(status):
    print("You " + status + "! Would you like to play again?")
    
    choice = input(" Y / N? ")

    if choice == "n":
            print("See you later!")
            exit()

    else:
        gameVars.playerLives = 5
        gameVars.computerLives = 5
        gameVars.player = False
