from flask import render_template, request, flash, redirect, url_for
from werkzeug.exceptions import abort
from fitness_service import FitnessService

class FitnessHandler:
    def __init__(self, storage):
        self.post_service = FitnessService(storage)

    def index(self):
        posts = self.post_service.get_all_posts()
        return render_template('index.html', posts=posts)

    def get_post(self, post_id):
        post = self.post_service.get_post_by_id(post_id)
        if post is None:
            abort(404)
        return render_template('post.html', post=post)

    def create(self):
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']

            if not title:
                flash('Title is required!')
            else:
                self.post_service.create_post(title, content)
                return redirect(url_for('index'))
        return render_template('create.html')

    def edit(self, post_id):
        post = self.post_service.get_post_by_id(post_id)

        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']

            if not title:
                flash('Title is required!')
            else:
                self.post_service.update_post(post_id, title, content)
                return redirect(url_for('index'))

        return render_template('edit.html', post=post)

    def delete(self, post_id):
        post = self.post_service.get_post_by_id(post_id)
        self.post_service.delete_post(post_id)
        flash('"{}" was successfully deleted!'.format(post['title']))
        return redirect(url_for('index'))
    
    
