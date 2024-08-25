import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('database.db')

# Create the schema directly in the Python script
connection.executescript('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL
    );
''')

# Create a cursor to interact with the database
cur = connection.cursor()

# Insert the posts into the 'posts' table
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post'))

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post'))

# Commit the transactions
connection.commit()

# Close the database connection
connection.close()
