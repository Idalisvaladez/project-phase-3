import argparse
from game.game_logic import Game
from game.player import Player 
from termcolor import cprint
from pyfiglet import Figlet
import time

def welcome():
    figlet = Figlet(font='isometric2', width= 200)
    cprint(figlet.renderText('The Escapist!'), 'green')
    time.sleep(1.0)

    

def main():
    parser = argparse.ArgumentParser(description='The Escapist Game CLI')
    parser.add_argument('create_player', nargs='?', default=None)
    args = parser.parse_args()

    # Initialize the game
    game = Game()
    
    player_name = input("Enter the player's name: ")
    try:
            # Create a new player
        player = Player(player_name)
        game.create_player(player)
        cprint(f"Player '{player_name}' created successfully.", 'green' , attrs=['bold'])
        with open('player.txt', 'w') as file:
            file.write(player_name)
    except ValueError as e:
        print(str(e))

    
def wall_one():
    cprint("After a day of sunbathing in the garden, Sofia needs to go to sleep.", 'yellow', attrs=["bold"])
    cprint("She walks through all the doors once and closes them behind her.", 'yellow', attrs=["bold"])
    cprint("Which room is her bedroom?", 'yellow', attrs=["bold"])
    cprint("              ____   _________   _____________   _____", 'green')
    cprint("              |   \  |        \   |         | \   F  |", 'green')
    cprint("              |      |            |    D    |__    __|", 'green')
    cprint("               /  A  |            |         |   \    |", 'green')
    cprint("              |       /           |        \         |", 'green')
    cprint("              |__  \_|            |__    \__|    G   |", 'green')
    cprint("              |      |      C     |         |        |", 'green')
    cprint("              |      |            |     E    \       |", 'green')
    cprint("              |   B  |            |         |___  \__|", 'green')
    cprint("              |      |             /       \      H  |", 'green')
    cprint("              |_  \____/__________|_________|________|", 'green')


if __name__ == "__main__":
    welcome()
    main()
    # wall_one()