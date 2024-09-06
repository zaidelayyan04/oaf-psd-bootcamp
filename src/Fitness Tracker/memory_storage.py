from abstract_storage import AbstractFitnessStorage

class MemoryStorage(AbstractFitnessStorage):
    def __init__(self):
        self.posts = []
        self.next_id = 1

    def get_all_posts(self):
        return self.posts

    def get_post_by_id(self, post_id):
        for post in self.posts:
            if post['id'] == post_id:
                return post
        return None

    def create_post(self, title, content):
        post = {
            'id': self.next_id,
            'title': title,
            'content': content
        }
        self.posts.append(post)
        self.next_id += 1

    def update_post(self, post_id, title, content):
        post = self.get_post_by_id(post_id)
        if post:
            post['title'] = title
            post['content'] = content

    def delete_post(self, post_id):
        post = self.get_post_by_id(post_id)
        if post:
            self.posts.remove(post)
