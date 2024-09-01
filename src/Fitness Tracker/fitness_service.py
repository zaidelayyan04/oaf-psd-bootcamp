# fitness_service.py
from abstract_storage import AbstractFitnessStorage

class FitnessService:
    def __init__(self, storage: AbstractFitnessStorage):
        self.storage = storage

    def get_all_posts(self):
        return self.storage.get_all_posts()

    def get_post_by_id(self, post_id):
        return self.storage.get_post_by_id(post_id)

    def create_post(self, title, content):
        self.storage.create_post(title, content)

    def update_post(self, post_id, title, content):
        self.storage.update_post(post_id, title, content)

    def delete_post(self, post_id):
        self.storage.delete_post(post_id)
