

class Game:
    def __init__(self):
        self.players = []

    def create_player(self, player):
        """Create a new player."""
        self.players.append(player)


    def find_player(self, player_name):
        """Find a player by name."""
        for player in self.players:
            if player.name == player_name:
                return player
        return None

    def show_inventory(self, player_name):
        """Show the inventory of a player."""
        player = self.find_player(player_name)
        if player:
            player.show_inventory()
        else:
            print(f"Player '{player_name}' not found.")