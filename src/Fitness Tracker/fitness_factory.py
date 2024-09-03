from fitness_service import FitnessService
from fitness_storage import FitnessStorage
from memory_storage import MemoryStorage
from abstract_factory import AbstractFitnessFactory
from fitness_handler import FitnessHandler

class ConcreteFitnessFactory(AbstractFitnessFactory):
    def __init__(self, use_memory = False):
        self.use_memory = use_memory

    def create_storage(self):
        if self.use_memory:
            return MemoryStorage()
        else:
            return FitnessStorage()

    def create_handler(self):
        storage = self.create_storage()
        service = FitnessService(storage)
        return FitnessHandler(service)
