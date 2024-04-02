"""
File: StepUp.py
Name:Rios Lu:
------------------------
This file shows Karel picking up 
the beeper at Street 1 Avenue 2,
putting it onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
"""

from karel.stanfordkarel import *


def main():
    move()
    pick_beeper()
    turn_left()
    move()
    turn_right()
    move()
    move()
    put99beepers()
    move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def put99beepers():
        for i in range(99):
            put_beeper()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
