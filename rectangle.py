class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            self.__dict__[name] = value

    def getArea(self):
        return self.width * self.height
a = Rectangle(3,4)
print(a.getArea())
