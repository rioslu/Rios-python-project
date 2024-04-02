"""
File: BeeperRowAdv.py
Name:Rios
------------------------------
This program makes Karel fill up
Street 1 with some beepers already
existed
"""
from karel.stanfordkarel import *
def main():
    """
    Karel will fill the first Street in any world
    """
    while front_is_clear():
        if on_beeper():
            put98beeper()
            move()
        else:
            put99beeper()
            move()
    if not on_beeper():
        put99beeper()
    else:
        put98beeper


def put98beeper():
    for i in range(98):
        put_beeper()


def put99beeper():
    for i in range(99):
        put_beeper()










####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)