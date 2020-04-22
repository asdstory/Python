class Turtle:
    def __init__(self, x):
        self.num = x

class Fish:
    def __init__(self, x):
        self.num = x

class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print("There are %d turtles and %d fishes in the pool!" % (self.turtle.num, self.fish.num))

a = Pool(3,8)
a.print_num()
