import codeblin_utils as cunt
import classes

MAIN_MENU = {'1': "Play", '2': "Help", '3': "Exit"}
running = True
choice = cunt.mainMenu(MAIN_MENU, "./res/logo.txt")

while running:

    if choice == '1':
        # TODO Start a new game
        print("Start")

    elif choice == '2':
        # TODO Add manual for game
        print("Help")

    elif choice == '3':
        exitPrompt = str(input("Are you sure? [Y]/[N]").lower())
        if exitPrompt == 'y':
            running = False

cunt.exitMsg()
