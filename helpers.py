from termcolor import cprint
from pyfiglet import Figlet
import inquirer
import time
from game.player import Player
from game.inventory import Inventory
import itertools




def welcome():
    figlet = Figlet(font='isometric2', width= 200)
    cprint(figlet.renderText('The Escapist!'), 'green')
    time.sleep(1.0)


def create_player():
    Player.create_table()
    Player.fetch_table()
    if len(Player.all) == 4:
        cprint("Already at max players, please select a prior one to replace", "red")
        questions = [
            inquirer.List('choice',
                message="Choose an option:",
                choices=[play.name for play in Player.all]
            )
        ]
        answers = inquirer.prompt(questions)
        choice = answers['choice']
        playerHold = None
        for play in Player.all:
            if play.name == choice:
                playerHold = play
        Player.remove_player(playerHold)
    name = input("Enter the new player's name: ")
    try:
        player = Player.create(name)
        cprint(f"Player '{player}' successfully created.", 'green' , attrs=['bold'])
        with open("player.db", 'a') as file:
            file.write(name)
        Inventory.drop_table()
        Inventory.create_table()

        Inventory.create("Bobby pin", player.id)
        Inventory.create("UN-sharpened pencil", player.id)
        Inventory.create("Loose change", player.id)
        Inventory.create("Chewed-up bubble gum", player.id)
    except Exception as exc:
        print("Error creating player: ", exc)



# Logic for if new player answer is No, that way they can choose an existing player out of
# the list of records in our Player table
def find_existing_player():
    Inventory.fetch_table()
    Player.fetch_table()
    player_choices = [
        inquirer.List('player',
                      message="Choose an existing player",
                      choices=[player for player in Player.all],
                    ),
    ]
    answers = inquirer.prompt(player_choices)
    chosen_player = answers['player']
    player = chosen_player
    if isinstance(player, Player):
        cprint(f'Welcome back {player}', "green")
        
    else:
        cprint("Error selecting player", "red")



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
    cprint("As you take a moment to collect yourself you come up with three possible options", attrs=["bold"])
    cprint("You can either: ", attrs=["bold"])
    time.sleep(2.0)

    options = [
        inquirer.List('option',
                      message="What will it be?",
                      choices=['Take a look around your jail cell', 'Check your pockets for any tools that could help you escape', 'Scream, cry, and beg for forgiveness'])
    ]

    answers = inquirer.prompt(options)
    chosen_option = answers['option']

    if chosen_option == 'Take a look around your jail cell':
        option_one()
    elif chosen_option == 'Check your pockets for any tools that could help you escape':
        # Implement logic for this option here
        pass
    elif chosen_option == 'Scream, cry, and beg for forgiveness':
        # Implement logic for this option here
        pass
    else:
        print("Not an answer choice")

def option_one():
    cprint("You get up to get a better look at your surroundings. You notice each wall has a different riddle.", attrs=["bold"])
    cprint("Standing in the middle your eyes dart back and forth to each wall.", attrs=["bold"])
    cprint("Instead of wasting anymore time you decide to just go for it and pick a wall to try.", attrs=["bold"])
    time.sleep(3.5)

    wall_choices = [
        inquirer.List('wall',
                      message="Which wall will it be?",
                      choices=['Wall 1', 'Wall 2', 'Wall 3'])
    ]

    answers = inquirer.prompt(wall_choices)
    chosen_wall = answers['wall']

    if chosen_wall == 'Wall 1':
        first_wall()
    elif chosen_wall == 'Wall 2':
        if "keyboard" in Inventory.all:
            second_wall()
        else:
            cprint("Looks like this wall needs some sort of tool to be accessed..", 'red', attrs=["bold"])
            option_one()
    elif chosen_wall == 'Wall 3':
        if "charger" in Inventory.all:
            third_wall()
        else:
            cprint("Looks like this wall needs some sort of tool to be accessed..", 'red', attrs=["bold"])
            option_one()
            
            
def option_two():
    cprint("Looking around again, you see the walls before you.", attrs=["bold"])
    time.sleep(3.5)

    wall_choices = [
        inquirer.List('wall',
                      message="Which wall will it be?",
                      choices=['Wall 1', 'Wall 2', 'Wall 3', 'Ask the guard to let you out.'])
    ]
    answers = inquirer.prompt(wall_choices)
    chosen_wall = answers['wall']
    
    if chosen_wall == 'Wall 1':
        first_wall_complete()
    elif chosen_wall == 'Wall 2':
        if "keyboard" in Inventory.all and "charger" in Inventory.all:
            cprint("You have already completed this wall. Try a different one!", 'white', attrs=["bold"])
            option_two()
        else:
            second_wall()
    elif chosen_wall == 'Wall 3':
        if "charger" not in Inventory.all:
            cprint("Looks like this wall needs some sort of tool to be accessed..", 'red', attrs=["bold"])
            option_two()
        elif "keyboard" in Inventory.all and "charger" in Inventory.all and "key" not in Inventory.all:
            third_wall()
        elif "keyboard" in Inventory.all and "charger" in Inventory.all and "key" in Inventory.all:
            cprint("You have already completed this wall. Time to leave!!", 'green', attrs=["bold"])
            option_three()
    elif chosen_wall == 'Ask the guard to let you out.':
        cprint("Not a chance!", 'red', attrs=["bold"])
        option_two()

        
            
    
def option_three():
    cprint("Looking around again, you see the walls before you.", attrs=["bold"])
    time.sleep(3.5)

    wall_choices = [
        inquirer.List('wall',
                      message="Which wall will it be?",
                      choices=['Wall 1', 'Wall 2', 'Wall 3', 'Ask the guard to let you out.', 'Open the cell with the key'])
    ]

    answers = inquirer.prompt(wall_choices)
    chosen_wall = answers['wall']

    if chosen_wall == 'Wall 1':
        first_wall_complete()
    elif chosen_wall == 'Wall 2':
        if "keyboard" in Inventory.all and "charger" not in Inventory.all:
            second_wall()
        else:
            if "keyboard" in Inventory.all and "charger" in Inventory.all:
                cprint("You have already completed this wall. Try a different one!", 'white', attrs=["bold"])
                option_two()
    elif chosen_wall == 'Wall 3':
        if "keyboard" in Inventory.all and "charger" in Inventory.all:
            third_wall()
        else:
            if "keyboard" in Inventory.all and "charger" in Inventory.all and "key" in Inventory.all:
                cprint("You have already completed this wall. Time to leave!!", 'green', attrs=["bold"])
                option_three()
    elif chosen_wall == 'Ask the guard to let you out.':
        cprint("Get out yourself!", 'red', attrs=["bold"])
    elif chosen_wall == 'Wall 3':
        if "keyboard" in Inventory.all and "charger" in Inventory.all and "key" in Inventory.all:
            game_win()

    
def first_wall_complete():
    cprint("You have already completed this wall. Try a different one!", 'white', attrs=["bold"])
    option_two()



def first_wall():
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
    questions = [
        inquirer.List('choice',
                      message="Choose an option:",
                      choices=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
                      default='A')
    ]
    answers = inquirer.prompt(questions)
    choice = answers['choice']
    if choice == "B":

        wall_one_invent()
    else:
        cprint("WRONG! Try again", "on_red", attrs=['bold'])
 
def wall_one_invent():
    cprint("CORRECT!", "white", "on_green", attrs=['bold'])
    cprint("                _______________________________________________",)
    cprint("            _-'    .-.-____________________________________.-.-- `-_ ",)
    cprint("          _-'.-.-. /---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-..--\  .-.-.`-_",)
    cprint("       _-'.-.-.-. /---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.`__\. .-.-.-.`-_",)
    cprint("    _-'.-.-.-.-. .-----.-.-.-.-.-[______]-.-.-.-.-.-.-.----. .-.-.-.-.`-_",)
    cprint(" _-'.-.-.-.-.-. .|_________________________________________|. .---.-.-.-.`-_",)
    cprint(":-----------------------------------------------------------------------------:",)
    cprint("`---._.-----------------------------------------------------------------._.---'",)
    cprint("                                                                                 ")
    cprint("A secret hatch opens on the wall and reveals a keyboard! Do you take it?", 'white', attrs=["bold"])
    questions = [
        inquirer.List('choice',
                      message="Choose an option",
                      choices=['Yes', 'No'],
                      default='Yes')
    ]
    answers = inquirer.prompt(questions)
    choice = answers['choice']
 
    if choice == "Yes":
        keyboard_clue()
    elif choice == 'No':
        cprint("Hint: riddles you solve give you tools along the way to help you escape", 'red', attrs=["bold"])
 
 
 
def keyboard_clue():
        cprint("You decide to take the keyboard. Now, let's choose an item to replace:", 'white', attrs=["bold"])
 
        # Create a list of item choices with IDs from Inventory.all
        item_choices = [(tool.name, tool.id) for tool in Inventory.all]
 
        inventory_choices = [
            inquirer.List('item',
                        message="Select an item to replace",
                        choices=[item[0] for item in item_choices]
            )
        ]
        item_answers = inquirer.prompt(inventory_choices)
 
        # Get the selected item's name
        selected_item_name = item_answers['item']
 
        # Find the item by name
        items = [tool for tool in Inventory.all if tool.name == selected_item_name]
 
        if items:
            # Use itertools.islice to get the item after the found item
            item_after = next(itertools.islice(Inventory.all, Inventory.all.index(items[0]) + 1, None), None)
 
            if item_after:
                item_after.update_invent("keyboard")  # Set the name to "keyboard"
                cprint(f"You have replaced {selected_item_name} with the keyboard!", 'green', attrs=["bold"])
                cprint(f"maybe you can use this somewhere..", 'white', attrs=["bold"])
                option_two()
            else:
                cprint("No item found after the selected item.", 'red', attrs=["bold"])

def second_wall():
    pass

def third_wall():
    pass

def game_win():
    pass