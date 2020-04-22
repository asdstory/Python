def mikes_magic_8():
    x = input("What do you offer for dinner? ")
    if len(x) <= 5:
        return "I'm gonna say no on this one"

    if x == "cheese?":
        return "Yes PLEASE!"

    if len(x) > 5:
        return "Maybe I can try."


mikes_magic_8()

import matplotlib.pyplot as plt
x = (1,2,3,4,5,6)
y = (1,4,9,16,25,36)
plt.plot(x,y)
plt.show()
help(plt)
