from termcolor import cprint
from pyfiglet import Figlet
import inquirer
import time
from game.player import Player
from game.inventory import Inventory
import itertools


current_player = 0


def welcome():
    figlet = Figlet(font='isometric2', width= 200)
    cprint(figlet.renderText('The Escapist!'), 'green')
    time.sleep(1.0)



def create_player():
    Player.create_table()
    Inventory.create_table()
    Player.fetch_table()
    if len(Player.all) == 4:
        cprint("Already at max players, please select a prior one to replace", "red")
        questions = [
            inquirer.List('choice',
                message="Choose an option",
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
    
    try:
        name = input("Enter the new player's name: ")
        player = Player.create(name)
        global current_player
        current_player = player.id
        print(current_player)
        cprint(f"Player '{player}' successfully created.", 'green', attrs=['bold'])
        # Fetch the existing items associated with the previous player (if any)
        existing_items = Inventory.fetch_table()
        
        Inventory.create("Bobby pin", player.id),
        Inventory.create("UN-sharpened pencil", player.id),
        Inventory.create("Loose change", player.id),
        Inventory.create("Chewed-up bubble gum", player.id)
        # Commit the changes to the database

    except Exception as exc:
        print("Error creating player: ", exc)




# Logic for if new player answer is No, that way they can choose an existing player out of
# the list of records in our Player table
def find_existing_player():
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
    global current_player 
    current_player = player.id
    print(current_player)
    start()

def start():
    print(f"Ready? {current_player}")
    questions = [
        inquirer.List('choice',
                      message="Choose an option:",
                      choices=['Yes', 'No'],
                      default='Yes')
    ]
    answers = inquirer.prompt(questions)
    choice = answers['choice'].lower()

    if choice == 'yes':
        storyline()
    elif choice == 'no':
        figlet = Figlet(font='ogre', width=100)
        cprint(figlet.renderText('Game Over!'), 'red', attrs=["bold"])



def storyline():
    print(current_player)
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
    time.sleep(.5)
    options_choice()


def options_choice():
    print(current_player)
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
    print(current_player)
    Inventory.fetch_table()
    inventory = [tool for tool in Inventory.all if tool.player_id == current_player]
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
        if "keyboard" in inventory:
            second_wall()
        else:
            cprint("Looks like this wall needs some sort of tool to be accessed..", 'red', attrs=["bold"])
            option_one()
    elif chosen_wall == 'Wall 3':
        if "charger" in inventory:
            third_wall()
        else:
            cprint("Looks like this wall needs some sort of tool to be accessed..", 'red', attrs=["bold"])
            option_one()
            
            
def option_two():
    Inventory.fetch_table()
    inventory = [tool for tool in Inventory.all if tool.player_id == current_player]
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
        if "keyboard" in inventory and "charger" in inventory:
            cprint("You have already completed this wall. Try a different one!", 'white', attrs=["bold"])
            option_two()
        else:
            second_wall()
    elif chosen_wall == 'Wall 3':
        if "charger" not in inventory:
            cprint("Looks like this wall needs some sort of tool to be accessed..", 'red', attrs=["bold"])
            option_two()
        elif "keyboard" in inventory and "charger" in inventory and "key" not in inventory:
            third_wall()
        elif "keyboard" in inventory and "charger" in inventory and "key" in inventory:
            cprint("You have already completed this wall. Time to leave!!", 'green', attrs=["bold"])
            option_three()
    elif chosen_wall == 'Ask the guard to let you out.':
        cprint("Not a chance!", 'red', attrs=["bold"])
        option_two()

        
            
    
def option_three():
    Inventory.fetch_table()
    inventory = [tool for tool in Inventory.all if tool.player_id == current_player]
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
        if "keyboard" in inventory and "charger" not in inventory:
            second_wall()
        else:
            if "keyboard" in inventory and "charger" in inventory:
                cprint("You have already completed this wall. Try a different one!", 'white', attrs=["bold"])
                option_two()
    elif chosen_wall == 'Wall 3':
        if "keyboard" in inventory and "charger" in inventory:
            third_wall()
        else:
            if "keyboard" in inventory and "charger" in inventory and "key" in inventory:
                cprint("You have already completed this wall. Time to leave!!", 'green', attrs=["bold"])
                option_three()
    elif chosen_wall == 'Ask the guard to let you out.':
        cprint("Get out yourself!", 'red', attrs=["bold"])
    elif chosen_wall == 'Wall 3':
        if "keyboard" in inventory and "charger" in inventory and "key" in inventory:
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
    Inventory.fetch_table()
    cprint("You decide to take the keyboard. Now, let's choose an item to replace:", 'white', attrs=["bold"])

        # Create a list of item choices with IDs from Inventory.all
    inventory = [tool for tool in Inventory.all if tool.player_id == current_player]
    print(inventory)
 
    inventory_choices = [
        inquirer.List('item',
                    message="Select an item to replace",
                    choices= set([item.name for item in inventory])
        )
    ]
    item_answers = inquirer.prompt(inventory_choices)
 
        # Get the selected item's name
    selected_item_name = item_answers['item']
 
        # Find the item by name
    items = [tool for tool in inventory if tool.name == selected_item_name]
 
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
    cprint("Your group enters another room, this hallway, longer than before, but with only one door", 'white', attrs=["bold"])
    cprint("You pass the door and at the end of the hall, you see a one way mirror with a Horse. Why ? Who knows. You should turn around", 'white', attrs=["bold"])
    # Modify the riddle and wall layout 
    cprint("Another interesting riddle description...", 'white', attrs=["bold"])
    cprint("              ___________________________________________", 'white')
    cprint("              |      |             |                    |", 'white')
    cprint("              |      |             |                    |", 'white')
    cprint("       --->       A  |      D                           |", 'white')
    cprint("              |      |             |                    |", 'white')
    cprint("              |      |__________   |___________________ |", 'white')
    cprint("              |      |      C      |                    |", 'white')
    cprint("              |      |             |                    |", 'white')
    cprint("              |      | _____/ \____|                    |", 'white')
    cprint("              |      |      B      |                    |", 'white')
    cprint("              |       _____________|____________________|  ", 'white')
    cprint("              |      |                                  | ",'white')
    cprint("              |      |< What Is The Meaning Of Life...?>|", 'white')
    cprint("              |      |     ---------------              | ", 'white')
    cprint("              |     /| \   ^__^                         |", 'white')
    cprint("              |     ||  \  (oo)\__________......        |", 'white')
    cprint("              |     \|     (__)\       )\/)             |", 'white')
    cprint("              |      |          ||      ||              |", 'white')
    cprint("______________|______|__________||______||______________|   ", 'white')
     
    questions = [
        inquirer.List('choice',
                      message="Choose an option:",
                      choices=['A', 'B', 'C', 'D',],
                      default='A')
    ]
    
    answers = inquirer.prompt(questions)
    choice = answers['choice']

    if choice == "D" :
        cprint("CORRECT!", "white", "on_green", attrs=['bold'])
        # Add any additional logic for a correct answer in the second wall
    else:
        cprint("TRY AGAIN!", 'white', 'on_red', attrs=["bold"])
        second_wall()


def third_wall():
    pass

def game_win():
    pass


#def second_wall():
    #logic built to have limited attempts on correct answer

    # Get the player's answer to the riddle
    #correct_answer = "d"  # Assuming the correct answer is "D"
    #max_attempts = 3
    #attempts = 0

    #while attempts < max_attempts:
        #questions = [
            #inquirer.Text('choice',
                           #message="Choose an option (A, B, C, D):",
                           #validate=lambda _, x: x.lower() in ['a', 'b', 'c', 'd'],
                           #,
        #]

        #answers = inquirer.prompt(questions)
        #choice = answers['choice'].strip().lower()

        #if choice == correct_answer:
            #cprint("CORRECT!", "white", "on_green", attrs=['bold'])
            # Add any additional logic for a correct answer in the second wall
            #break  # Exit the loop if the answer is correct
        #else:
            #attempts += 1
            #remaining_attempts = max_attempts - attempts
            #cprint(f"TRY AGAIN! {remaining_attempts} attempts remaining.", 'white', 'on_red', attrs=["bold"])

    #else:
        #cprint("Sorry, you've run out of attempts. Game over!", 'red', attrs=["bold"])
        # might want to handle the game over scenario here