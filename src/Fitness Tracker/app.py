# app.py
from flask import Flask
from fitness_handler import FitnessHandler
from fitness_storage import FitnessStorage 
from fitness_service import FitnessService
from memory_storage import MemoryStorage

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

memory = MemoryStorage()
storage = FitnessStorage('database.db') 
handler = FitnessHandler(storage)

@app.route('/')
def index():
    return handler.index()

@app.route('/post/<int:post_id>')
def get_post(post_id):
    return handler.get_post(post_id)

@app.route('/create', methods=['GET', 'POST'])
def create():
    return handler.create()

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    return handler.edit(post_id)

@app.route('/delete/<int:post_id>')
def delete(post_id):
    return handler.delete(post_id)

if __name__ == '__main__':
    app.run(debug=True)
