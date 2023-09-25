from termcolor import cprint
from pyfiglet import Figlet
import time
from game.player import Player




def welcome():
    figlet = Figlet(font='isometric2', width= 200)
    cprint(figlet.renderText('The Escapist!'), 'green')
    time.sleep(1.0)


def create_player():
    Player.create_table()
    Player.fetch_table()
    print(Player.all)
    if len(Player.all) != 4:
        name = input("Enter the new player's name: ")
        player = Player.create(name)
        cprint(f"Player '{player}' successfully created.", 'green' , attrs=['bold'])
        with open("player.db", 'a') as file:
            file.write(name)
    else:
        cprint("Already at max players, please select one to replace by inputing the corresponding number", "red")
        for play in Player.all:
            print(f"{play.id + 1} - {play.name}")
        replaced = input(">")
        try:
            replaced = int(replaced)
        except Exception as exc:
            print("Error selecting player, likely not ID number: ", exc)
        print(replaced)
        if isinstance(replaced,int) and 0 < replaced:
            Player.remove_player_by_id(Player.all[replaced - 1].id)
            name = input("Enter the new player's name: ")
            try:
                player = Player.create(name)
                cprint(f"Player '{player}' successfully created.", 'green' , attrs=['bold'])
                with open("player.db", 'a') as file:
                    file.write(name)
            except Exception as exc:
                print("Error creating player: ", exc)
        else:
            print("Invalid ID number")



def find_player_by_name():
    name = input("Enter player's name: ")
    player = Player.find_player(name)
    print(player) if player else print(
        f'Player {name} not found'
    )



def storyline():
    cprint("You wake up being tossed into a Jail Cell. When you ask the guards why? They say...", "light_cyan", attrs=["bold"])
    time.sleep(3.0)
    cprint("           ________________                        ________________________________________________", 'light_cyan')
    cprint("           \      __      /         __         .-- You're guilty of stealing other people's code! --.", 'light_cyan')
    cprint("            \_____()_____/         /  )       ( The only way to redeem yourself is by solving all the )", 'light_cyan')
    cprint("            '============`        /  /       (   riddles on the wall. In doing so, you'll earn a key  )", 'light_cyan')
    cprint("            #---\  /---#         /  /        (                 that can set you free!!              _)", 'light_cyan')
    cprint("            (# @\| |/@ #)       /  /         | ,---------------------------------------------------'", 'light_cyan')
    cprint("             \   (_)   /       /  /          |/", 'light_cyan')
    cprint("             |\ '---` /|      /  /", 'light_cyan')
    cprint("     _______/  \_____/  \____/ o_|", 'light_cyan')
    cprint("    /       \  /     \  /   / o_|", 'light_cyan')
    cprint("   / |           o|        / o_| \ ", 'light_cyan')
    cprint("  /  |  _____     |       / /   \ \ ", 'light_cyan')
    cprint(" /   |  |===|    o|      / /\    \ \ ", 'light_cyan')
    cprint("|    |   \@/      |     / /  \    \ \ ", 'light_cyan')
    cprint("|    |___________o|__/----)   \    \/ ", 'light_cyan')
    cprint("|    '              ||  --)    \     |", 'light_cyan')
    cprint("|___________________||  --)     \    /", 'light_cyan')
    cprint("     |           o|   ''''   |   \__/", 'light_cyan')
    cprint("     |            |          |", 'light_cyan')


def options_choice():
    time.sleep(3.0)
    cprint("As you take a moment to collect yourself you come up with three possible options")
    cprint("You can either: ")
    time.sleep(2.0)
    cprint("1. Take a look around your jail cell.")
    cprint("2. Check your pockets for any tools that could help you escape.")
    cprint("3. Scream, cry, and beg for forgiveness.")
    option = input("What will it be? ")
    if option == 1:
        option_one()
    elif option == 2:
        pass
    elif option == 3:
        pass
    else:
        print("Not an answer choice")

def option_one():
    cprint("You get up to get a better look at your surroundings. You notice each wall has a different riddle.")
    cprint("Standing in the middle your eyes dart back and forth to each wall.")
    cprint("Instead of wasting anymore time you decide to just go for it and pick a wall to try.")
    time.sleep(3.5)
    cprint("Try wall: 1")
    cprint("Try wall: 2")
    cprint("Try wall: 3")
    wall = input("Which wall will it be? ")
    if wall == 1:
        wall_one()
    elif wall == 2:
        pass
    elif wall == 3:
        pass


def first_wall():
    wall_one()
    choice = input("> ")
    if choice == "B":
        cprint("CORRECT!", "white", "on_green", attrs=['bold'])
    else:
        cprint("TRY AGAIN!", 'white', 'on_red', attrs=["bold"])

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








