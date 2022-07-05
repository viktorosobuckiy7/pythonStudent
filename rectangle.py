class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        return self.width*self.height

    def __add__(self, other):
        return self.square() + other.square()

    def __gt__(self, other):
        return self.square() > other.square()

    def sub(self):
        n = int(input("n = "))
        return self.square()*n


