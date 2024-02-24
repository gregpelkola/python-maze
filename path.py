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

def print_maze(stdscr, maze, path=[]):
    GREEN = curses.color_pair(1)
    PURPLE = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            stdscr.addstr(i, j*2, value, GREEN)

def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return (i, j)
    return None

def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_PURPLE, curses.COLOR_BLACK)
    #green_and_black = curses.color_pair(1)

    
    stdscr.clear()
    print_maze(maze, stdscr)
    stdscr.refresh()
    stdscr.getch()

wrapper(main)