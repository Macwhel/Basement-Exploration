# this is to help draw stuff

class Rectangle:
    def __init__(self, y, x, width):
        self.x = x
        self.y = y
        self.x2 = x + width
        self.y2 = y + width
        self.color = 'black'

    # Drawable coordinates
    def setColor(self, newColor):
        self.color = newColor