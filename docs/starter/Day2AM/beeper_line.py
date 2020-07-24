from karel.stanfordkarel import *

"""
File: beeper_line_karel.py
------------------------------
Places a row of beepers on the bottom row of Karel's world.
Works with any size world.

This program is already completed for you. Try running it!
"""


def main():
    while front_is_clear():
        put_beeper()
        move()

    # the line below is necessary to place the final beeper.
    # the number of times Karel moves is one less than the number
    # of times Karel places a beeper (if the world is five squares
    # wide, we place 5 beepers, but only move 4 times).
    put_beeper()

if __name__ == "__main__":
    run_karel_program()
