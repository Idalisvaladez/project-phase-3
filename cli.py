import argparse
from game.game_logic import Game
from game.player import Player 

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
        print(f"Player '{player_name}' created successfully.")
        with open('player.txt', 'w') as file:
            file.write(player_name)
    except ValueError as e:
        print(str(e))

if __name__ == "__main__":
    main()
