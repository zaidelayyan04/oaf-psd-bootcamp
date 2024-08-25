from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from fitness_service import FitnessService
from fitness_handler import FitnessHandler


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dog'

service = FitnessService()
handler = FitnessHandler(service)

@app.route('/')
def index():
   return handler.index()

@app.route('/<int:post_id>')
def post(post_id):
   return handler.get_post(post_id)

@app.route('/create', methods=('GET', 'POST'))
def create():
   return handler.create()

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    return handler.edit(id)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    return handler.delete(id)

if __name__ == '__main__':
    app.run(debug=True)