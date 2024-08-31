# sqlite_storage.py
import sqlite3
from abstract_storage import AbstractFitnessStorage

class SQLiteFitnessStorage(AbstractFitnessStorage):
    def __init__(self, db_path='database.db'):
        self.db_path = db_path

    def get_db_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def get_all_posts(self):
        conn = self.get_db_connection()
        posts = conn.execute('SELECT * FROM posts').fetchall()
        conn.close()
        return posts

    def get_post_by_id(self, post_id):
        conn = self.get_db_connection()
        post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
        conn.close()
        return post

    def create_post(self, title, content):
        conn = self.get_db_connection()
        conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
        conn.commit()
        conn.close()

    def update_post(self, post_id, title, content):
        conn = self.get_db_connection()
        conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?', (title, content, post_id))
        conn.commit()
        conn.close()

    def delete_post(self, post_id):
        conn = self.get_db_connection()
        conn.execute('DELETE FROM posts WHERE id = ?', (post_id,))
        conn.commit()
        conn.close()
