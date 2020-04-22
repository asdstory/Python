import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print("My position is: ", self.x, self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("I am so many food to eat^_^")
            self.hungry = False
        else:
            print("I am full！")

a = Fish()
print('I am a fish.')
a.move()
b = Goldfish()
print('I am a goldfish.')
b.move()
c = Shark()
print('I am a Shark.')
c.move()
c.eat()
