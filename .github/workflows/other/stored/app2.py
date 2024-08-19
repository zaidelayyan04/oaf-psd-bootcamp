from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('workout_logger.db')

@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.cursor()
    # Query to get total workouts and total weight lifted
    cursor.execute('SELECT COUNT(*) FROM Workouts')
    total_workouts = cursor.fetchone()[0]

    cursor.execute('''
    SELECT SUM(Exercises.weight * Exercises.sets * Exercises.reps)
    FROM Exercises
    ''')
    total_weight = cursor.fetchone()[0] or 0

    conn.close()
    return render_template('index.html', total_workouts=total_workouts, total_weight=total_weight)

@app.route('/log', methods=['GET', 'POST'])
def log_workout():
    if request.method == 'POST':
        exercise = request.form['exercise']
        sets = request.form['sets']
        reps = request.form['reps']
        weight = request.form['weight']

        conn = connect_db()
        cursor = conn.cursor()

        # Assume user_id is 1 for simplicity
        cursor.execute('INSERT INTO Workouts (user_id, date) VALUES (?, ?)', (1, datetime.now().strftime('%Y-%m-%d')))
        workout_id = cursor.lastrowid
        cursor.execute('INSERT INTO Exercises (workout_id, name, sets, reps, weight) VALUES (?, ?, ?, ?, ?)', 
                       (workout_id, exercise, sets, reps, weight))

        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('log_workout.html')

if __name__ == '__main__':
    app.run(debug=True)
