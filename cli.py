import argparse
from game.player import Player
from game.inventory import Inventory 
from pyfiglet import Figlet
from termcolor import cprint
import inquirer
import time

from helpers import (
    welcome,
    storyline,
    create_player,
    find_player_by_name,
    options_choice,
    option_one
)

def main():
    print("New player?")
    questions = [
        inquirer.List('choice',
                      message="Choose an option:",
                      choices=['Yes', 'No'],
                      default='Yes')
    ]
    answers = inquirer.prompt(questions)
    choice = answers['choice'].lower()
    
    if choice == 'yes':
        create_player()
    elif choice == 'no':
        find_player_by_name()



def start():
    print("Ready?")
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
        time.sleep(.5)
        options_choice()
        option_one()
    elif choice == 'no':
        figlet = Figlet(font='ogre', width=100)
        cprint(figlet.renderText('Game Over!'), 'red', attrs=["bold"])



if __name__ == "__main__":
    welcome()
    main()
    start()