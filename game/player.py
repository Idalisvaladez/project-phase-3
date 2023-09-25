from game.__init__ import CONN, CURSOR

class Player:
    # dict to store all player instances to a database
    all = {}

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
    def drop_table(cls):
        """Drop the persisted Player object"""
        sql = """
            DROP TABLE IF EXISTS players;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Player row added with name of current instance created"""
        sql = """
            INSERT INTO players (name)
            VALUES (?);
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    
    @classmethod
    def create(cls, name):
        """Initialize a new player and save to database"""
        player = cls(name)
        player.save()
        return player
    

    @classmethod
    def db_instance(cls, row):
        """Return player with matching attribute value from the table"""
        player = cls.all.get(row[0])
        if player:
            player.name = row[1]
        else:
            player = cls(row[1])
            player.id = row[0]
            cls.all[player.id] = player
        return player

    @classmethod
    def find_player(cls, name):
        """Find a player by name."""
        sql = """
            SELECT *
            FROM players
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.db_instance(row) if row else None
       

