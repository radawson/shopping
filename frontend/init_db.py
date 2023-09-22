import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO items (item, description) VALUES (?, ?)",
            ('eggs', '24 eggs')
            )

cur.execute("INSERT INTO items (item, description) VALUES (?, ?)",
            ('english muffin', '6 pack original english muffin')
            )

connection.commit()
connection.close()