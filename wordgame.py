# Version 1

print('--------------This is a word game #1--------------')
temp = input("Guess the number I have in my mind: ")
guess = int(temp)
if guess == 8:
    print("Great?!")
    print("Anyway, there is no bonus!")
else:
    print("No, it is 8!")
print("Game Over^_^")

# Version 2

import random
secret = random.randint(1,10)
print('--------------This is a word game--------------')
temp = input("Guess the number I have in my mind: ")
guess = int(temp)
while guess != secret:
    temp = input("No, try again: ")
    guess = int(temp)
    if guess == secret:
        print("Great?!")
        print("Anyway, there is no bonus!")
    else:
        if guess > secret:
            print("Too big!")
        else:
            print("Too small!")
print("Game Over^_^")
