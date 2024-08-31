from abc import ABC, abstractmethod

class AbstractFitnessStorage(ABC):
    @abstractmethod
    def get_all_posts(self):
        pass

    @abstractmethod
    def get_post_by_id(self, post_id):
        pass

    @abstractmethod
    def create_post(self,title, content):
        pass
    @abstractmethod
    def update_post(self, post_id, title, contnt):
        pass

    @abstractmethod
    def delete_post(self, post_id):
        pass
    


