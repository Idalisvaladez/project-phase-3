import argparse
from game.player import Player
from game.inventory import Inventory 
from pyfiglet import Figlet
from termcolor import cprint
import time

from helpers import (
    welcome,
    wall_one,
    storyline,
    create_player,
    find_player_by_name
)

def main():
    cprint("New player?")
    choice = input("[y/ N]")
    if choice == "y":
        create_player()
    elif choice == "N":
        find_player_by_name()
    # parser = argparse.ArgumentParser(description='The Escapist Game CLI')
    # parser.add_argument('create_player', nargs='?', default=None)
    # args = parser.parse_args()

    # # Initialize the game
    # game = Game()
    
    # player_name = input("Enter the player's name: ")

    # try:
    #         # Create a new player
    #     player = Player(player_name)
    #     game.create_player(player)
    #     cprint(f"Player '{player_name}' created successfully.", 'green' , attrs=['bold'])
    #     with open('player.txt', 'w') as file:
    #         file.write(player_name)
    # except ValueError as e:
    #     print(str(e))

def start():
    cprint("Ready?")
    choice = input("[y/ N] > ")
    if choice == 'y':
        storyline()
    elif choice == 'N':
        figlet = Figlet(font='ogre', width= 100)
        cprint(figlet.renderText('Game Over!'), 'red', attrs=["bold"])


def first_wall():
    time.sleep(0.5)
    wall_one()
    choice = input("> ")
    if choice == "B":
        cprint("CORRECT!", "white", "on_green", attrs=['bold'])
    else:
        cprint("TRY AGAIN!", 'white', 'on_red', attrs=["bold"])


if __name__ == "__main__":
    welcome()
    main()
    start()