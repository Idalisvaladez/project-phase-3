class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def __str__(self):
        return f"Player: {self.name}"

    def add_item_to_inventory(self, item):
        """Add an item to the player's inventory."""
        self.inventory.append(item)

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