"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:K is at(1,2), facing east
    post-condition:K will get to(7,2), facing east
    """
    for i in range(3):
        dive()
        put99beeper()
        jump()


def dive():
    """
    K is on top of
    """
    move()
    turn_right()
    move()


def jump():
    turn_left()
    turn_left()
    move()
    turn_right()
    move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def put99beeper():
    for i in range(99):
        put_beeper()





# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
