#A script file that welcomes the user given to it. If no name was given,
#then it welcomes the whole world.

import sys

#define the name
def hello():
    global name
    name = "World"

    # if you write just your first name
    if len(sys.argv) == 2:
        name = sys.argv[1]

    # if you write your first and last name
    elif len(sys.argv) > 2:
        name = sys.argv[1] + " " + sys.argv[2]


#print on the screen
def screen():
    print("Hello " + name + "!")


hello()
screen()
