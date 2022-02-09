from abc import abstractmethod
from .place import Place

class VideoPlace(Place):
    def __init__(self, id, name, video):
        super().__init__(id, name)
        self.video = video
    def display(self):
       print("Here I am displaying video class with ", self.id, self.name, self.video)
