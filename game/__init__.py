import sqlite3

CONN = sqlite3.connect('player.db')
CURSOR = CONN.cursor()