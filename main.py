from places.textplace import TextPlace
from places.videoplace import VideoPlace

p = {TextPlace(1,"Place1", "My Text"), VideoPlace(2,"Place2", "My Video")}

for o in p:
    o.display()