import argparse
from game.player import Player
from game.inventory import Inventory 
from pyfiglet import Figlet
from termcolor import cprint
import inquirer
import time

from helpers import (
    welcome,
    start,
    create_player,
    find_existing_player,
)

def main():
    Player.drop_table()
    Inventory.drop_table()
    welcome()
    print("New player?")
    questions = [
        inquirer.List('choice',
                      message="Choose an option",
                      choices=['Yes', 'No'],
                      default='Yes')
    ]
    answers = inquirer.prompt(questions)
    choice = answers['choice'].lower()
    
    if choice == 'yes':
        create_player()
        start()
    elif choice == 'no':
        find_existing_player()




if __name__ == "__main__":
    main()