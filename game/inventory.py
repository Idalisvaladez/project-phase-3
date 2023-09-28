from game.__init__ import CONN, CURSOR

class Inventory:
    all = []

    def __init__(self, name, player_id, id=None):
        self.name = name
        self.id = id
        self.player_id = player_id

    def __repr__(self):
        return f'{self.name}'
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY,
            name TEXT,
            player_id INTEGER,
            FOREIGN KEY (player_id) REFERENCES players(id))
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def fetch_table(cls):
        SQLfetch = CURSOR.execute("SELECT * FROM inventory").fetchall()
        for tool in SQLfetch:
            print(tool)
            cls.create_nonDB(tool[1],tool[0]-1, tool[2]-1)
        CONN.commit()
        print(cls.all)
        
    @classmethod
    def create_nonDB(cls, name, id, player_id):
        """Initialize a new player and save to database"""
        tool = cls(name, player_id, id )
        tool.save_nonDB()
        return tool
    
    def save_nonDB(self):
        type(self).all.append(self)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS inventory;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO inventory (name, player_id)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.player_id+1))
        CONN.commit()

        self.id = CURSOR.lastrowid-1
        type(self).all.append(self)
    
    def update(self):
        sql = """
            UPDATE inventory
            SET player_id = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.player_id, self.id))
        CONN.commit()
        
    def update_invent(self, replacement_name):
        sql = """
            UPDATE inventory
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (replacement_name, self.id + 1))
        CONN.commit()
        type(self).create_nonDB(replacement_name,self.id,self.player_id)
        type(self).all.pop(type(self).all.index(self))

    @classmethod
    def delete(cls, inventory):
        sql = """
            DELETE FROM inventory
            WHERE id = ?
        """
        CURSOR.execute(sql, (inventory.id,))
        CONN.commit()

        cls.all.pop(cls.all.index(inventory))

    @classmethod
    def delete_by_player(cls, player_id):
        sql = """
            DELETE FROM inventory
            WHERE player_id = ?
        """
        CURSOR.execute(sql, (player_id,))
        CONN.commit()

        for tool in [tool for tool in cls.all if tool.player_id == player_id]:
            cls.all.pop(cls.all.index(tool))

    @classmethod
    def create(cls, name, player_id):
        tool = cls(name, player_id)
        tool.save()
        return tool
    
    @classmethod
    def in_db(cls, row):
        tool = cls.all.index(row[0])
        if tool:
            tool.name = row[1]
            tool.player_id = row[2]
        else:
            tool = cls(row[1], row[2])
            tool.id = row[0]
            cls.all[tool.id] = tool
        return tool
    
    # @classmethod
    # def tools(cls):
    #     sql = """
    #         SELECT *
    #         FROM players
    #         JOIN inventory 
    #         ON players.id = inventory.player_id;
    #     """
    #     CURSOR.execute(sql)
    #     return [row[0] for row in CURSOR.fetchall()]
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM inventory
            WHERE name = ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.in_db(row) if row else None

    
    @classmethod
    def find_by_id(cls, item_id):
        sql = """
            SELECT *
            FROM inventory
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (item_id,)).fetchone()
        return cls.in_db(row) if row else None
    



