# CUNT: Codeblin's Ultra Necessary Toolkit
import os, time, random, shutil
# import os

TERM_COLS, TERM_ROWS = shutil.get_terminal_size()

# Clears the terminal
def clear():

    if os.name == "nt":
        os.system('cls')
    elif os.name == "posix":
        os.system('clear')

# Print centered text in stoud
def printc(text, end='\n'):
    print(text.center(TERM_COLS), end=end)

# Initializes the program
# ---Args---
# logo -> logo.txt
def printLogo(logo: str):
    clear()
    with open(logo) as f:
        for i in f:
            printc(i)

# Prints main menu options
def mainMenu(menu: dict, logo: str):
    while True:
        printLogo(logo)
        time.sleep(1)
        for i, j in menu.items():
            printc(f"[{i}] {j}")

        menuChoice = input("\n>>> ")
        if menuChoice in menu.keys():
            return menuChoice

# Exits the program with a message
def exitMsg():
    printc("Thanks for playing!")
    time.sleep(1)
    printc("Visit www.codeblins.online for more fun stuff!")
    time.sleep(1)
    printc("psyborg0ne, used to be an adventurer like you since 1997")
    time.sleep(1)
    exit()
