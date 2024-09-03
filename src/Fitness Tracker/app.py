from flask import Flask
from fitness_factory import ConcreteFitnessFactory

app = Flask(__name__)
app.secret_key = 'dog'

# True for use_memory storage and false for sqlite3 storage
service = ConcreteFitnessFactory(use_memory=False)  
handler = service.create_handler()

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
