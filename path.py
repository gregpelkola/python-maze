import curses
from curses import wrapper
import queue
import time

maze = [
    ["O", "#", "#", "#", "#", " ", " ", " ", " "],
    [" ", "#", " ", " ", " ", " ", "#", "#", " "],
    [" ", "#", " ", "#", "#", "#", "#", "#", " "],
    [" ", "#", " ", "#", "#", "#", "#", "#", "X"],
    [" ", "#", " ", " ", " ", " ", "#", "#", "#"],
    [" ", "#", "#", " ", "#", " ", " ", "#", "#"],
    [" ", "#", " ", " ", "#", "#", "#", "#", "#"],
    [" ", " ", " ", "#", "#", "#", " ", " ", "#"],
    ["#", "#", " ", " ", " ", " ", " ", "#", "#"]
]

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Welcome to the maze!")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)