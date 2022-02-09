from abc import abstractmethod
from .place import Place

class TextPlace(Place):
    def __init__(self, id, name, text):
        super().__init__(id, name)
        self.text = text
    def display(self):
        print("Here I am displaying text class with ", self.id, self.name, self.text)
