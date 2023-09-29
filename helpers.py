from termcolor import cprint
from pyfiglet import Figlet
import inquirer
import time
from game.player import Player
from game.inventory import Inventory
import itertools
import simpleaudio as sa

wav_object = sa.WaveObject.from_wave_file("Sounds/Prison_Cell_Door.wav")
winner = sa.WaveObject.from_wave_file("Sounds/Yay_-_Sound_Effect.wav")
guard = sa.WaveObject.from_wave_file("Sounds/Cartoon_Mumble_Speak_-_Sound_Effect_HQ.wav")
BGM = sa.WaveObject.from_wave_file("Sounds/BGM.wav")
# background_music = sa.WaveObject.from_wave_file("")

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
        cprint("Already at max players, please select a prior one to replace", "red", attrs=['bold'])
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
        Inventory.delete_by_player(playerHold.id)
        Player.remove_player(playerHold)
    
    try:
        name = input("Enter the new player's name: ")
        player = Player.create(name)
        global current_player
        current_player = player.id
        cprint(f"Player '{player}' successfully created.", 'green', attrs=['bold'])
        
        Inventory.create("bobby pin", player.id),
        Inventory.create("un-sharpened pencil", player.id),
        Inventory.create("loose change", player.id),
        Inventory.create("chewed-up bubble gum", player.id)
        # Commit the changes to the database

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
    global current_player 
    current_player = player.id
    start()

def start():
    questions = [
        inquirer.List('choice',
                      message="Ready?",
                      choices=['Yes', 'No'],
                      default='Yes')
    ]
    answers = inquirer.prompt(questions)
    choice = answers['choice'].lower()

    if choice == 'yes':
        storyline()
    elif choice == 'no':
        create_player()




def storyline():
    wav_object.play()
    BGM.play()
    cprint("You wake up being tossed into a Jail Cell. When you ask the guards why? They say...", "white", "on_blue", attrs=["bold"])
    time.sleep(3.0)
    guard.play()
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
    # background_music.play()
    options_choice()


def options_choice():
    time.sleep(3.0)
    cprint("As you take a moment to collect yourself you come up with three possible options", "blue", attrs=["bold"])
    time.sleep(2.0)

    options = [
        inquirer.List('option',
                      message="You can either",
                      choices=['Take a look around your jail cell', 'Check your pockets for any tools that could help you escape', 'Scream, cry, and beg for forgiveness'])
    ]

    answers = inquirer.prompt(options)
    chosen_option = answers['option']

    if chosen_option == 'Take a look around your jail cell':
        option_one()
    elif chosen_option == 'Check your pockets for any tools that could help you escape':
        tools_storyline()
        utilize_tools()
    elif chosen_option == 'Scream, cry, and beg for forgiveness':
        beg()
    else:
        print("Not an answer choice")

def option_one():
    inventory = [tool for tool in Inventory.all if tool.player_id == current_player]
    cprint("You get up to get a better look at your surroundings. You notice each wall has a different riddle.", "blue", attrs=["bold"])
    time.sleep(1.0)
    cprint("Standing in the middle your eyes dart back and forth to each wall.",'blue', attrs=["bold"])
    time.sleep(1.0)
    cprint("Instead of wasting anymore time you decide to just go for it and pick a wall.", 'blue', attrs=["bold"])
    time.sleep(1.0)

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
    inventory = [tool for tool in Inventory.all if tool.player_id == current_player]
    has_keyboard = any(tool.name == "keyboard" for tool in inventory)
    has_charger = any(tool.name == "charger" for tool in inventory)
    has_key = any(tool.name == 'key' for tool in inventory)
    cprint("Let's try a different one this time.",'blue', attrs=["bold"])
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
        if has_keyboard and has_charger:
            cprint("You have already completed this wall. Try a different one!", 'blue', attrs=["bold"])
            option_two()
        else:
            second_wall()
    elif chosen_wall == 'Wall 3':
        if not has_charger:
            cprint("Looks like this wall needs some sort of tool to be accessed..", 'red', attrs=["bold"])
            option_two()
        elif has_charger and has_keyboard and has_key not in inventory:
            cprint("You walk over the the third wall and notice your reflection bounce back from the wall.","blue", attrs=["bold"])
            cprint("Upon closer inspection you realize the wall is actually a giant computer screen!","blue", attrs=["bold"])
            cprint("But the battery is dead and there's no keyboard. Maybe your tools can help you here...","blue", attrs=["bold"])
            third_wall()
        elif has_keyboard and has_charger and has_key:
            cprint("You have already completed this wall. Time to leave!!", 'green', attrs=["bold"])
            option_three()
    elif chosen_wall == 'Ask the guard to let you out.':
        cprint("Not a chance!",'red', attrs=["bold"])
        option_two()

        
            
    
def option_three():
    inventory = [tool for tool in Inventory.all if tool.player_id == current_player]
    cprint("Now that I have more tools, maybe there's a better option...","blue", attrs=["bold"])
    time.sleep(3.5)

    wall_choices = [
        inquirer.List('wall',
                      message="Which will it be?",
                      choices=['Wall 1', 'Wall 2', 'Wall 3', 'Ask the guard to let you out', 'Open the cell with the key'])
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
                cprint("You have already completed this wall. Try a different one!", "red", attrs=["bold"])
                option_two()
    elif chosen_wall == 'Wall 3':
        if "keyboard" in inventory and "charger" in inventory:
            third_wall()
        else:
            if "keyboard" in inventory and "charger" in inventory and "key" in inventory:
                cprint("You have already completed this wall. Time to leave!!", 'green', attrs=["bold"])
                option_three()
    elif chosen_wall == 'Ask the guard to let you out':
        cprint("Get out yourself!", 'red', attrs=["bold"])
        option_three()
    elif chosen_wall == 'Open the cell with the key':
        if "keyboard" in inventory and "charger" in inventory and "key" in inventory:
            game_win()

    
def first_wall_complete():
    cprint("You have already completed this wall. Try a different one!", "red", attrs=["bold"])
    option_two()


def first_wall():
    cprint("After a day of sunbathing in the garden, Sofia needs to go to sleep.", 'white','on_blue', attrs=["bold"])
    cprint("She walks through all the doors once and closes them behind her.", 'white','on_blue', attrs=["bold"])
    cprint("Which room is her bedroom?", 'white', 'on_blue', attrs=["bold"])
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
        one_wrong()

def one_wrong():
    cprint("WRONG! Try again", "grey", "on_red", attrs=['bold'])
    first_wall()
 
def wall_one_invent():
    cprint("CORRECT!", "grey", "on_green", attrs=['bold'])
    cprint("                _______________________________________________",)
    cprint("            _-' .-.-____________________________________.-.-- `-_ ",)
    cprint("          _-'.-.-. /---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-..--\  .-.-.`-_",)
    cprint("       _-'.-.-.-. /---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.`__\. .-.-.-.`-_",)
    cprint("    _-'.-.-.-.-. .-----.-.-.-.-.-[______]-.-.-.-.-.-.-.----. .-.-.-.-.`-_",)
    cprint(" _-'.-.-.-.-.-. .|_________________________________________|. .---.-.-.-.`-_",)
    cprint(":-----------------------------------------------------------------------------:",)
    cprint("`---._.-----------------------------------------------------------------._.---'",)
    cprint("                                                                                 ")
    cprint("A secret hatch opens on the wall and reveals a keyboard! Do you take it?", 'blue', attrs=["bold"])
    correct_answer = "Yes"
    while True:
        questions = [
            inquirer.List('choice',
                          message="Choose an option",
                          choices=['Yes', 'No'],
                          default='Yes')
        ]
        answers = inquirer.prompt(questions)
        choice = answers['choice']

        if choice == correct_answer:
            keyboard_clue()
            break
        else:
            cprint("You should really take it!", 'red', attrs=["bold"])
 
 
 
def keyboard_clue():
    cprint("You decide to take the keyboard. Now, let's choose an item to replace:", 'blue', attrs=["bold"])

        # Create a list of item choices with IDs from Inventory.all
    inventory = [tool for tool in Inventory.all if tool.player_id == current_player]
 
    inventory_choices = [
        inquirer.List('item',
                    message="Select an item to replace",
                    choices= [item.name for item in inventory]
        )
    ]
    item_answers = inquirer.prompt(inventory_choices)
 
        # Get the selected item's name
    selected_item_name = item_answers['item']
 
        # Find the item by name
    items = [tool for tool in inventory if tool.name == selected_item_name and tool.player_id == current_player]
    items[0].update_invent("keyboard")  # Set the name to "keyboard"
    cprint(f"You have replaced {selected_item_name} with the keyboard!", 'green', attrs=["bold"])
    cprint(f"maybe you can use this somewhere..", 'blue', attrs=["bold"])
    option_two()

def second_wall():
    cprint("Your group enters a long hallway, you see a one way mirror with a Horse. Why ? Who knows.", 'white', 'on_blue', attrs=["bold"])
    cprint("The horse says you can free him, but stay in jail, or break into Room C, and gain an item to help you, but there are no hard feelings. ", 'white','on_blue', attrs=["bold"])
    time.sleep(1.0)
    cprint("Which room do you break into? ", 'white', 'on_blue', attrs=["bold"])
    time.sleep(2.0)
    cprint("And do you still feel guilt free ?", 'red', attrs=["bold"])
    cprint("              ___________________________________________", 'white')
    cprint("              |      |             |                    |", 'white')
    cprint("              |      |             |                    |", 'white')
    cprint("       --->       A  |      C      |       *item*       |", 'white')
    cprint("              |      |             |                    |", 'white')
    cprint("              |      |_____/ \_____|____________________|", 'white')
    cprint("              |      |             |                    |", 'white')
    cprint("              |      |             |                    |", 'white')
    cprint("              |      |             |                    |", 'white')
    cprint("              |      |      B      |  *free the horsey* |", 'white')
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
                      choices=['A', 'B', 'C'],
                      default='A')
    ]
    
    answers = inquirer.prompt(questions)
    choice = answers['choice']

    if choice == "C" :
        cprint("CORRECT!", "grey", "on_green", attrs=['bold'])
        charger_clue()
        
    else:
        cprint("TRY AGAIN!", 'grey', 'on_red', attrs=["bold"])
        second_wall()


def charger_clue():
    inventory = [tool for tool in Inventory.all if tool.player_id == current_player]
    ascii_charger = '''
                                         ,','
                                        ; ;
                                        `.`.
                                          ) ;
                                     ,,,-','
                      _____,,,,---''",,,-'
            ___,,--'""_____,,,,--''""
    __,,--'"__,,--'"""
 ,-"_,,--'""
; ,'       
; ;         
`.``-..-----;;;;|==
  ``--...___;;;;|==
    '''
    cprint(ascii_charger, )
    cprint("You find a charger! Now, let's choose an item to replace:", 'blue', attrs=["bold"])
    item_choices = [tool for tool in Inventory.all if tool.player_id == current_player]

    inventory_choices = [
        inquirer.List('item',
                      message="Select an item to replace",
                      choices= [item.name for item in item_choices]
        )
    ]
    item_answers = inquirer.prompt(inventory_choices)

    
    selected_item_name = item_answers['item']

    items = [tool for tool in inventory if tool.name == selected_item_name and tool.player_id == current_player]
    items[0].update_invent("charger")

    cprint(f"You have replaced {selected_item_name} with the charger!", 'green', attrs=["bold"])
    cprint(f"Maybe you can use this somewhere..", 'blue', attrs=["bold"])
    option_two()


def second_wall_completed():
    cprint("You have successfully completed the second wall!",'green', attrs=["bold"])
    option_two()  



def third_wall():
    item_choices = [tool for tool in Inventory.all if tool.player_id == current_player]

    inventory_choices = [
        inquirer.Checkbox('item',
                      message="Select a tool to use",
                      choices= [item.name for item in item_choices]
        )
    ]
    item_answers = inquirer.prompt(inventory_choices)
    choice = item_answers['item']

    if 'charger' in choice and 'keyboard' in choice:
        cipher()
    else:
        cprint("Those won't really help me here...", "blue", attrs=['bold'])
        third_wall()
    
def cipher():
    cprint("You use the charger to power up the screen on this wall. The screen lights up and displays a message...", 'blue', attrs=["bold"])
    cprint("Another interesting riddle to decipher...", 'blue', attrs=["bold"])    
    ascii_art = r'''
                 _______________________________________________________
                |                                                       |
                |                                                       |
                |                                                       |
                |                                                       |
                |                           3                           |
                |                                                       |
                |                                                       |
                |                w k h f d n h l v d o l h              |
                |                                                       |
                |                           <                           |
                |                                                       |
                |                                                       |
                |                                                       |
                |                     Enter answer                      |
                |                                                       |
                |                                                       |
                |                                                       |
                |_______________________________________________________|
                '''
                
    cprint(ascii_art, 'white')
    
    max_attempts = 3  # Maximum number of allowed attempts
    attempts = 0  # Initialize the attempts counter

    while attempts < max_attempts:
        questions = [
            inquirer.Text('answer', message="Enter the secret phrase:")
        ]

        answers = inquirer.prompt(questions)

        user_input = answers['answer']

        if user_input == "the cake is a lie":
            cprint("You solved it!", 'green', attrs=["bold"])
            cprint("The screen now shows an image resembling a key, and as you watch, it materializes before your eyes, gently descending into your open palm.", 'blue', attrs=["bold"])
            key_art()
            cprint("This key looks like it fits the cell door..", 'blue')
            key_clue()
            break
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            cprint(f"Wrong answer. You have {remaining_attempts} {'attempts' if remaining_attempts > 1 else 'attempt'} left.", 'red')
            

    if attempts >= max_attempts:
        cprint("You've run out of attempts.", 'red', attrs=["bold"])
        figlet = Figlet(font='ogre', width=100)
        cprint(figlet.renderText('Game Over!'), 'red', attrs=["bold"])


            
def key_art():
    ascii_art = r'''
                .--.
               /.-. '----------.
               \'-' .--"--""-"-'
                '--'
    '''

    cprint(ascii_art, 'white')
    
            
def key_clue():
    cprint("You decide to take the key. Now, let's choose an item to replace:", 'blue', attrs=["bold"])

    # Create a list of item choices with IDs from Inventory.all
    inventory = [tool for tool in Inventory.all if tool.player_id == current_player]

    inventory_choices = [
        inquirer.List('item',
                      message="Select an item to replace",
                      choices=set([item.name for item in inventory])
                      )
    ]
    item_answers = inquirer.prompt(inventory_choices)

    # Get the selected item's name
    selected_item_name = item_answers['item']

    # Find the item by name
    items = [tool for tool in inventory if tool.name == selected_item_name and tool.player_id == current_player]
    items[0].update_invent("key")  # Set the name to "keyboard"
    cprint(f"You have replaced {selected_item_name} with a key!", 'green', attrs=["bold"])
    option_three()





def tools_storyline():
    cprint("You eagerly reach into your pockets to see what you can find", "blue", attrs=['bold'])
    cprint("Looking at your hands you notice 4 small items", "blue", attrs=['bold'])
    ascii_tools = r'''
              _.-._                  _.-._
            /| | | |_              _| | | |\
            || | | | |            | | | | ||
            || | | | |            | | | | ||
          _ ||  @@    |          |    ==D  || _
          \\`\        ;          ;         /`//
           \\      V  |          |    0o    //
            \\      /              \      //
            | |    |               |     | |
            | |    |               |     | |
        '''
    cprint(ascii_tools, "white")
    cprint("A Bobby pin, some Loose change, an UN-sharpened pencil, and a Chewed-up bubble gum.", "blue", attrs=['bold'])
    time.sleep(1.5)
    cprint("You start thinking... ")
    time.sleep(1)
    cprint("Maybe there's some way I can utilize one of these tools to escape...")

def utilize_tools():
    questions = [
        inquirer.List('choice',
                      message="Wan't to try using one of these tools?",
                      choices=['Yes', 'No'],
                    ),
    ]
    
    answers = inquirer.prompt(questions)
    choice = answers['choice'].lower()

    if choice == "yes":
        tools_choice()
    elif choice == "no":
        cprint("You think to yourself there's no way any of these items can help me right now", "blue", attrs=['bold'])
        cprint("Time to go back to my other options...", "blue", attrs=['bold'])
        options_choice()


def tools_choice():
    questions = [
            inquirer.List('choice',
                      message="How are you breaking out of here?",
                      choices=['Pick the jail cell lock with your bobby pin', 'Bribe the guards with your loose change', 'Use the UN-sharpened pencil to reach for the keys off the guards waist ', 'Use the gums stickiness to spider-man your way out'],
            ),
        ]
    
    answers = inquirer.prompt(questions)
    selection = answers['choice']
    if selection == 'Pick the jail cell lock with your bobby pin':
            cprint("You were Unsuccessful! Looks like you just wasted time! Go back to starting options", 'red', attrs=['bold'])
            options_choice()
    elif selection == 'Bribe the guards with your loose change':
            cprint("HAHA HAHA! The guards all laughed in your face. Go back to starting options", 'red', attrs=['bold'])
            options_choice()
    elif selection == 'Use the UN-sharpened pencil to reach for the keys off the guards waist ':
            cprint("Oh no! The UN-sharpened pencil wasn't long enough to reach! Go back to starting options", 'red', attrs=['bold'])
            options_choice()
    elif selection == 'Use the gums stickiness to spider-man your way out':
            cprint("OUCH! The stickiness wore off and you fell face first! Go back to starting options", 'red', attrs=['bold'])
            options_choice()
    else:
        print("Error")

def beg():
    ascii_beg = r'''
       _.-._
     /| | | |_
     || | | | |
     || | | | |
    _||     ` |
   \\`\       ;
    \\        |
     \\      /
     | |    |
     | |    |
    '''
    cprint(ascii_beg, 'white')
    time.sleep(2.0)
    cprint("The guards stream recorded you and now you're going viral on all social media platforms.", 'blue', attrs=['bold'])
    time.sleep(1.5)
    ascii_phone = r'''
               
                   # # # # # # # # # 
                #                     #
                #                        #
                #                          #
                #        =====     =====    #
                #         | |      | |      #
                #         | |      | |      #
                #              ~           #                    ___________
                #                         #                    ||          ||
              #                        #                       ||          ||
            #                 #   #                           _||          ||  _
            #      ##        (                               (_||          || ( |
            #   #   #---------#                              (_||          || / /
            #     #   #__#  # #                              (_||          ||   )
            #      ##__|   #    #                              ||          ||  (
            #           )   #    #                            (|_____--_____|   \
            #           #   #    #                                      \        \
            #         #    #    #                                        \        \
            #_______# #____#___#
                                    
    '''
    cprint(ascii_phone, 'white')
    cprint("Even if you escape your reputation will forever be tainted.", 'blue', attrs=['bold'])
    options_choice()

def game_win():
    wav_object.play()
    ascii_win = '''                                                                                                                                                                                                                                                                      
                     @=*=-:.                                                                                                                  
                     @ .--=+*:@@@@@@@@@@@#- :.                                                                                                
                  -@@@ .--:-- @@          @@-@@@@@@@@@@@@@@@@@+-=:.                                                                           
               +@@@@*+: ----- @@          @         :@        @--*#%@#@@@@@@@@@#@%@@+.                                                        
            @@@@%-..-*= --:-- @@          @+         @        @       @-      @      @= -*%@@@@@%@@@@%*+.                                     
            @@  ..-:-++ ----- @@   @.--.@ @@ @@*@%@#@@=@@@%+- @       *:      @ .+%#=@+@@@#@#**@+@%.@*+@.@@@@@@%@@                            
            +@- :::=-+* ----- *@.  @    : =@  +   :  @ %    + @ @   @@@@* @  @@ @  + % @   @   @ %  @  # % @ @ :%*                            
             @@ -=:=:**.-----.:@=  @    ..:@  @   :: @ @    + @ @   @@.*  %  *@ %  # @ %   @   @ @  @ *# @ %.@ =@                             
             @@ ::-+:*+::----: @=  %     + @  @   .+ @ @    * @ @   @@ %  @  %@ %  @ @ *   @   @ @ -@ @  @ .@# +@                             
             #@:.:=:--*-.=---- @=  .:    # @  @    = @ +    : @ #   @% *  %  %% *  @ @ =  -@   @ @ @. @  @= @- *@                             
             :@:  .:=+*= =---- @@-*@@+%%-@ @+.@=@@#@:@-@#@%@@.@:@*@-@% @%=@  @% -  % -    **  :  % @  @ @ @ @ :%=                             
              @@@@#-  -= ----- @@   @    @ @  @    @ @ .      @ *   @@=%  %  @+    @-+@@@#@*- @ =: @  # @ %:@ -@                              
              @@ -+@@@*=.-=---.=@   @  . @ @- @:*#-@ @:@@@@@@:@ **@-=  #@@@@@@@@@@@@@%@#%-%*%@@=@@@@#@@+@ =%@ =@                              
              @@ :---#*+:-==--: @@**@=%%-@ @@ @:   @ @      - @@    @@@@  *    =      %   @.  @ @  % @  %**@* *#                              
              #@-.=--=*+=:=-=-= @-  @    . @* =    @ @      = @@@@@+   *  * -  @  @.  @   @   @ @ %= @ - @ @..@-                              
               @% =:==*==:=-=== @@ +@%%@#@=@@ @@#@.@ @*#@*%%@ @@ =#@@@@- :%*@# @  %   @   @   @ @ @  @ @-@-@.:@                               
               @# :-*=#==:===== @@  *-     @@ .:   @ @  .   + @@ +==++@@:*+ @  @ *@@@@@  -@     #+#%%%+-  @@-=@                               
               @@* -==**=--==== %@  .@    **@  @   @ @- +   % @@ ====-%+:#@ @  @  @  .@  @@.@@@%####*++**-  .+@                               
               +@:*# -+#==-====.=@   @    %=@  @   @ @- =   = @@.-+++=%+:## @  @  @  @.  :    -=*++++=+++#*=:#=       @@@#@@@                 
                @% %%::*+=--=-=:-@   @    = @  @   @ @% @@@@@:@@::+=++#*:*= @  @  @  @  @#%=*+-@*++==+==++*++@       .-@@@@@=                 
                @@ ==@+.=+-====-:@# -@#@@%@#@#+@:= @ @# %   : %@.:*+++#+:#+.@%@@  -  @  @@@%@@@#+*++++++++***@      #@@@@@                    
   .::::......  %@::-+*@.=-====- @@  @    + @  @   : @# +   + %@ -*=+=#+-#- @  @ +@@#@   @@@@#**####******##@@         @%                     
  .::-::....    *@: +==*@--===== @@  +    - @  @@@@@@@@@@@@@@ @@++#=++#=-#- @ =# ..  @ @@@@@=##############%@@      *@@@                      
   :=++=--...    @@  +=+#---==== - =@@@@@@@ @= #     -@ -   + @@ -%=**#=-#  # *+ *+ .@  =  @= @%#########%%@@     *@@@@                       
   .-=++****+-:  @@=+:+*#+=-==== @@         @- @%@@@@@@+@%#=+ @@# #+%:#:=%@@# %: #: +%  @@ @@-%@@%#######@@@=    @@@@                         
    .::::=+**##* @@ %  ##++:==== =@:@@@@@@@.@# :     .@     - @@+%  @*#-=@  :*@%-@  +=  @* @@@= @@@@@@@@@%     @@@@@                          
   .::--:....-=+:#@=*#* @#+:--==: @         @@ -     -@ +   = @@.@@- +@*=@ .     @@@@   @  %@@@    @@% -**=@@@@@@@                            
   .::---:::.:-: -@ =+@- *+=-=--: @.  #     #@ -.     @ .   * @@ +@@@  *+@ .  *  :  :+@@@#. %@@@@*   -**%@@@@@@                               
   .:::-:-::.:--. =:.**@===+--=== @#  *      @     -*=@*@@@%* @@= **@**==@+=  +  %  *   @:%@ =@@@@#-::---%@@:                                 
   .::---::-:.:--.*=: #%%*:+-==== @@  *.-#%@*@-@@%+.  @       @@+*--*=@-+@ @@@@  =  %   @  : +%@@@@@#+++%@@.                                  
   .:::---:::.:--.+*.- ##%+====== %@*@@+.    @        @%@@@@@@@@.@-*@-%.+@ =  %@@@  =  +@  # @ @#%%%%%%@@ *:                                  
   ..:::::::-::--:=#- *:#+%:=====::@         @.@@@@@@:@       @@.**#*:@.+@ =  -  *@@@  :@  @ # @######%@@@@                                   
   .:--------::.::-#@-.-@#@.=====- @-@@@@@@@*@      : @*%@%=- @@ =*+=-@.*@#-  . .   -@@@@  - #@%++**##@@  .                                   
   .:::----:-:-::-:++@   =@-=-===- @*      : @@%@%*:= @     - @@.+++@:@:*# @@@         @#-=:*@%***####@. .-                                   
   :---------:-:...*=%%:+-+#-===== @@-@@@@+- @: -   = @ .     @@.=++*=*:#*    %@: =%@@@@. -@@%########@  ::                                   
   .:::::---------:++.@*.--@====== @@  :   : @@ *:  = @ .=*@@ @@.*++-**:#- -=@@@@@@@     =@@%#**##**+#*@                                      
   :--======----::.-#-.@=:- ====++ @@  *-. . %% --+%@*@%#*-.. @@:#+++@*-%@@@:      -@@%: @@#**####*==@+=%=                                    
  .:-=====----::::.:+@*+@==#+++++=.@@  :  .+=@@*@#+.. @     -=@@ *#*-@.=@  +@@     .  :*=@%#**%@@@@@@@%*+@.                                   
   :==+=++++=+==-::.-=#-%%.==+++++:*@-#@@%*- =@       @@%@@@@@%@* #* @==@    -@@+  .     @%##@@@     #%@%@@+                                  
  .:==++++===+++++=-++**.#+ -=++==-:@  :.    :@ =*@@@@@@%%*-  .@@.@@ %:=@:      %@@     @@%@@@#    @*@#*%@@@@                                 
   :-==============-=+=#++@*=-====- @    -*@@@@@@@@+. :.     .+#@# = #==@ %%:       =@@@@#@@@  =*:.@@@@@@@@=                                  
   .:-----===++++++=+#%*#+#@*-===== @@@@@@@@=..       =+ .--:.+=:@#@#%==@  -@%:   +#@@%@@@@=      @@@#%#                                      
   ..:.:.:::::----===*@@@@#@@+=*#@@@@         -.   .  ++.:----#%-#@  *=+@    :%@. @@@@@@%         @@+*@@                                      
                       :-===@@@@@*. ..       .+-  ... ==::::..=+  %@%@*+@ ..   .:@@@@@.   :=++=*#= @@@@@                                      
                                    :=.   .  .+-  ... --    .-#%+-=@. -*@ .....  @+ .=%..+*%@@#=--  =.                                        
                      ..-:--. ......:=:   .. .=-      :=-*%@@@#+-: =@++*@ ...... *@+..*#%%*=--=+***==:: . .                                   
                       .-:::.. .... .-:       :.  .-=*#%%#*=::+*+-::#%#@@ .. ....  @@@@**+===++=++*#@#+:.......                               
                        .:::-:..... .:.       :=+#**+-:.    ..=*#+**%@@%   ..:::.::.    -++=-:::-=++*#%#+=-:::::..                            
                         ...::......... .:-==+--.      .      .::.   :=-. ..::::..:-==.   .-=======------::::..:::..                          
                         ....:....  .::--::.          ..       .        ...........:-=-:::-==--:-----::............:....                      
                           ....                                ...:.............. ..::----:.  . ..::::...............:....                    
                                                           ....:........       ..::.::::..         .                                                                                                                                                                                                                                                                                         
    '''
    cprint(ascii_win, "white")
    winner.play()

