from termcolor import cprint
from pyfiglet import Figlet
import time
from game.player import Player




def welcome():
    figlet = Figlet(font='isometric2', width= 200)
    cprint(figlet.renderText('The Escapist!'), 'green')
    time.sleep(1.0)



def storyline():
    cprint("You wake up being tossed into a Jail Cell. When you ask the guards why? They say...", "light_cyan", attrs=["bold"])
    time.sleep(2.0)
    cprint("   ___________               ________________________________________________", "light_cyan", attrs=["bold"])
    cprint(" _|   _____   |_          .-- You're guilty of stealing other people's code! --.", "light_cyan", attrs=["bold"])
    cprint(" |    \ * /    |         ( The only way to redeem yourself is by solving all the )", "light_cyan", attrs=["bold"])
    cprint(" |    (___)    |        (   riddles on the wall. In doing so, you'll earn a key  ) ", "light_cyan", attrs=["bold"])
    cprint("\_______________/       (                 that can set you free!!              _)", "light_cyan", attrs=["bold"])
    cprint(" (    \    /    )       | ,---------------------------------------------------'", "light_cyan", attrs=["bold"])
    cprint(" /    O    O    \       |/", "light_cyan", attrs=["bold"])
    cprint("/____    ^   ____\ ", "light_cyan", attrs=["bold"])
    cprint(" |      ~       |", "light_cyan", attrs=["bold"])
    cprint("  \_ _ _  _ _ _/", "light_cyan", attrs=["bold"])
    cprint("  ..__|    |__.. ", "light_cyan", attrs=["bold"])
    cprint(" /          *   \ ", "light_cyan", attrs=["bold"])



def wall_one():
    cprint("After a day of sunbathing in the garden, Sofia needs to go to sleep.", 'white', attrs=["bold"])
    cprint("She walks through all the doors once and closes them behind her.", 'white', attrs=["bold"])
    cprint("Which room is her bedroom?", 'white', attrs=["bold"])
    cprint("              ____   _________   _____________   _____", 'white')
    cprint("              |   \  |        \   |         | \   F  |", 'white')
    cprint("              |      |            |    D    |__    __|", 'white')
    cprint("               /  A  |            |         |   \    |", 'white')
    cprint("              |       /           |        \         |", 'white')
    cprint("              |__  \_|            |__    \__|    G   |", 'white')
    cprint("              |      |      C     |         |        |", 'white')
    cprint("              |      |            |     E    \       |", 'white')
    cprint("              |   B  |            |         |___  \__|", 'white')
    cprint("              |      |             /       \      H  |", 'white')
    cprint("              |_  \____/__________|_________|________|", 'white')


def create_player():
    Player.create_table()
    name = input("Enter the player's name: ")
    print(type(name))
    try:
        player = Player.create(name)
        cprint(f"Player '{player}' successfully created.", 'green' , attrs=['bold'])
        with open("player.db", 'a') as file:
            file.write(name)
    except Exception as exc:
        print("Error creating player: ", exc)

def find_player_by_name():
    name = input("Enter player's name: ")
    player = Player.find_player(name)
    print(player) if player else print(
        f'Player {name} not found'
    )
