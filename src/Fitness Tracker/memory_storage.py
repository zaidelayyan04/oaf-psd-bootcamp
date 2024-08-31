from abstract_storage import AbstractFitnessStorage

class MemoryStorage(AbstractFitnessStorage):
    def __init__(self):
        self.posts = {}
        self.next_id = 1

    def get_all_posts(self):
        return list(self.posts.values())
    
    def get_post_by_id(self, post_id):
        return super().get_post_by_id(post_id)
    
    def create_post(self, title, content):
        self.posts[self.counter] = {'id': self.counter, 'title': title, 'content': content}
        self.counter += 1

    def update_post(self, post_id, title, content):
        if post_id in self.posts:
            self.posts[post_id] = {'id': post_id, 'title': title, 'content': content}

    def delete_post(self, post_id):
        if post_id in self.posts:
            del self.posts[post_id]
