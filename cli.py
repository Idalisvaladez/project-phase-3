import argparse
from game.player import Player
from game.inventory import Inventory 
from pyfiglet import Figlet
from termcolor import cprint
import time

from helpers import (
    welcome,
    storyline,
    create_player,
    find_player_by_name,
    options_choice,
)

def main():
    cprint("New player?")
    choice = input("[y/ N] >  ")
    if choice == "y":
        create_player()
    elif choice == "N":
        find_player_by_name()



def start():
    cprint("Ready?")
    choice = input("[y/ N] >  ")
    if choice == 'y':
        storyline()
        time.sleep(3.5)
        options_choice()
    elif choice == 'N':
        figlet = Figlet(font='ogre', width= 100)
        cprint(figlet.renderText('Game Over!'), 'red', attrs=["bold"])




if __name__ == "__main__":
    welcome()
    main()
    start()