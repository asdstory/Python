class Turtle: # Python class should use First Upper letter
    """A simple class"""
    # Properties
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = 'BigMouth'

    # Method
    def climb(self):
        print("I am climbing......")

    def run(self):
        print("I am running......")

    def bite(self):
        print("Bite you!")

    def eat(self):
        print("So happy I have something to eat^_^")

    def sleep(self):
        print("Good night, Zzzz")
a = Turtle()
a.climb()
a.run()
a.bite()
a.eat()
a.sleep()
