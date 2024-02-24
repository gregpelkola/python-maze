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
        else:
            stdscr.addstr(i, j*2, value, PURPLE)

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

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze [row][col] == end:
            return path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)

def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0: # Up
        neighbors.append((row - 1, col))
    if row < len(maze) -1: # Down
        neighbors.append((row + 1, col))
    if col > 0: # Left
        neighbors.append((row, col - 1))
    if col < len(maze[0]) - 1: # Right
        neighbors.append((row, col + 1))
    return neighbors



def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_PURPLE, curses.COLOR_BLACK)

    path = find_path(maze, stdscr)
    print_maze(stdscr, maze, path)
    stdscr.getch()

wrapper(main)