from game.__init__ import CONN, CURSOR

class Player:
    # dict to store all player instances to a database
    all = []

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return (
            f'<Player {self.id} : {self.name}>'
        )

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) < 15:
            self._name = name
        else:
            raise ValueError(
                "Player name must be a non-empty string"
            )
    
    @classmethod
    def create_table(cls):
        """Create a new table to persist Player attributes"""
        sql = """
            CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def fetch_table(cls):
        SQLfetch = CURSOR.execute("SELECT * FROM players").fetchall()
        for player in SQLfetch:
            cls.create_nonDB(player[1],player[0]-1)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the persisted Player object"""
        sql = """
            DROP TABLE IF EXISTS players;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save_nonDB(self):
        type(self).all.append(self)

    @classmethod
    def create_nonDB(cls, name, id):
        """Initialize a new player and save to database"""
        player = cls(name,id)
        player.save_nonDB()
        return player


    def save(self):
        """Player row added with name of current instance created"""
        sql = """
            INSERT INTO players (name)
            VALUES (?);
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all.append(self)
        

    
    @classmethod
    def create(cls, name):
        """Initialize a new player and save to database"""
        player = cls(name)
        player.save()
        return player
    
    @classmethod
    def all_players(cls):
        sql = """
            SELECT *
            FROM players
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.db_instance(row) for row in rows]
    

    @classmethod
    def db_instance(cls, row):
        """Return player with matching attribute value from the table"""
        player = cls.all.index(row[0])
        if player:
            player.name = row[1]
        else:
            player = cls(row[1])
            player.id = row[0]
            cls.all[player.id] = player
        return player

    @classmethod
    def find_by_id(cls, name):
        """Find a player by id."""
        sql = """
            SELECT *
            FROM players
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.db_instance(row) if row else None
       

    @classmethod
    def remove_player(cls,player):
        """Removes the player from the database based on the ID"""
        CURSOR.execute("DELETE FROM players WHERE id=?",(player.id+1,))
        CONN.commit()

        cls.all.pop(cls.all.index(player))
