import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(

    roll INTEGER PRIMARY KEY,

    name TEXT NOT NULL,

    math INTEGER,

    science INTEGER,

    english INTEGER

)
""")

connection.commit()

connection.close()

print("Database Created Successfully!")