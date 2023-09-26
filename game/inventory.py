import sqlite3

CONN = sqlite3.connect('player.db')
CURSOR = CONN.cursor()

class Inventory:
    all = []

    def __init__(self, player_id):
        self.player_id = player_id
        Inventory.all.append(self)

    @property
    def tools(self):
        sql = """
            SELECT tools.name
            FROM inventory
            JOIN tools ON inventory.tool_id = tools.id
            WHERE inventory.player_id = ?
        """
        CURSOR.execute(sql, (self.player_id,))
        return [row[0] for row in CURSOR.fetchall()]

    def add_tool(self, tool_name):
        sql = """
            INSERT INTO inventory (player_id, tool_id)
            VALUES (?, (SELECT id FROM tools WHERE name = ?));
        """
        try:
            CURSOR.execute(sql, (self.player_id, tool_name))
            CONN.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def remove_tool(self, tool_name):
        sql = """
            DELETE FROM inventory
            WHERE player_id = ? AND tool_id = (SELECT id FROM tools WHERE name = ?);
        """
        CURSOR.execute(sql, (self.player_id, tool_name))
        CONN.commit()


    #def add_item_to_inventory(self, item):
        #"""Add an item to the player's inventory."""
        #Inventory.all.append(item)

    #def remove_item_from_inventory(self, item_name):
        #"""Remove an item from the player's inventory by name."""
        #for item in self.inventory:
            #if item.name == item_name:
                #self.inventory.remove(item)
                #return True
        #return False

    #def show_inventory(self):
        #"""Display the player's inventory."""
        #if not self.inventory:
            #print(f"{self.name}'s inventory is empty.")
        #else:
            #print(f"{self.name}'s inventory:")
            #for item in self.inventory:
                #print(f"- {item}")

    # def show_inventory(self, name):
    #     """Show the inventory of a player."""
    #     player = self.find_player(name)
    #     if player:
    #         player.show_inventory()
    #     else:
    #         print(f"Player '{name}' not found.")