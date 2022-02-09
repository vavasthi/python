from abc import abstractmethod
from .base import Base

class Place(Base):
    def __init__(self, id, name):
        self.id = id
        self.name = name
    @abstractmethod
    def display(self):
        pass