class Inventory:

    all = []

    def __init__(self, name):
        self.name = name
        Inventory.all.append(self)

    def __str__(self):
        return f"Tool: {self.name}"

    def add_item_to_inventory(self, item):
        """Add an item to the player's inventory."""
        Inventory.all.append(item)

    def remove_item_from_inventory(self, item_name):
        """Remove an item from the player's inventory by name."""
        for item in self.inventory:
            if item.name == item_name:
                self.inventory.remove(item)
                return True
        return False

    def show_inventory(self):
        """Display the player's inventory."""
        if not self.inventory:
            print(f"{self.name}'s inventory is empty.")
        else:
            print(f"{self.name}'s inventory:")
            for item in self.inventory:
                print(f"- {item}")

    # def show_inventory(self, name):
    #     """Show the inventory of a player."""
    #     player = self.find_player(name)
    #     if player:
    #         player.show_inventory()
    #     else:
    #         print(f"Player '{name}' not found.")