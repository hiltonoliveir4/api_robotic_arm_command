import sqlite3

conn = sqlite3.connect('robotic-arm.db')
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE commands(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        command varchar(4) NOT NULL
    );
    """
)

conn.close()