import sqlite3

def create_tables():
    conn = sqlite3.connect('workout_logger.db')
    cursor = conn.cursor()

    # Create Users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')

    # Create Workouts table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Workouts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        date TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(id)
    )
    ''')

    # Create Exercises table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Exercises (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        workout_id INTEGER,
        name TEXT NOT NULL,
        sets INTEGER,
        reps INTEGER,
        weight REAL,
        FOREIGN KEY (workout_id) REFERENCES Workouts(id)
    )
    ''')

    conn.commit()
    conn.close()

# Call this function when the app starts or during setup
create_tables()
