from abc import ABC, abstractmethod

class AbstractFitnessFactory(ABC):
    @abstractmethod
    def create_storage(self):
        pass

    @abstractmethod
    def create_handler(self):
        pass
