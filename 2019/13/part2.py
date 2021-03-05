import sys
sys.path.append("C:/Users/Admin/Documents/Code/advent_of_code/2019/13")
sys.path.append("C:/Users/Admin/Documents/Code/advent_of_code/AoC_tools")
import IntCode as ic
from aoc_tools import display_grid

code = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/13/input.txt')
# play for free
code[0] = 2
prog = ic.Intcode(code)

def read_instructions(instructions):
    tiles = {}
    pos = 0
    while pos < len(instructions):
        x = instructions[pos]
        y = instructions[pos + 1]
        tile_id = instructions[pos + 2]
        if not x == -1:
            tiles[(x, y)] = tile_id
        elif x == -1:
            current_score = tile_id
        pos += 3
    return tiles

def get_score(instructions):
    tiles = {}
    pos = 0
    while pos < len(instructions):
        x = instructions[pos]
        y = instructions[pos + 1]
        tile_id = instructions[pos + 2]
        if not x == -1:
            tiles[(x, y)] = tile_id
        elif x == -1:
            current_score = tile_id
        pos += 3
    return current_score

def show_grid(instructions):
    tiles = read_instructions(instructions)
    # print(len(block_tiles))
    # print(block_tiles)

    # assert len(block_tiles) == 239

    # display the grid
    lookup_table = {0: ' ', 1: 'W', 2: 'B', 3: '-', 4: 'O'}
    display_grid(tiles, lookup_table)

def get_ball(instructions):
    tiles = read_instructions(instructions)
    for key, value in tiles.items():
        if value == 4:
            ball = key
    return ball

def get_paddle(instructions):
    tiles = read_instructions(instructions)
    for key, value in tiles.items():
        if value == 3:
            paddle = key
    return paddle

def count_blocks(instructions):
    tiles = read_instructions(instructions)
    block_tiles = [key for key, value in tiles.items() if value == 2]
    return len(block_tiles)

while True:
    prog.run(reset=False)
    ball = get_ball(prog.output)
    paddle = get_paddle(prog.output)
    n = count_blocks(prog.output)
    if ball[0] < paddle[0]:
        prog.run(input=-1, reset=False)
        n_prev = n
        n = count_blocks(prog.output)
        if n != n_prev:
            show_grid(prog.output)
            print("blocks left:", n)
            print("score:", get_score(prog.output))
    elif ball[0] > paddle[0]:
        prog.run(input=1, reset=False)
        n_prev = n
        n = count_blocks(prog.output)
        if n != n_prev:
            show_grid(prog.output)
            print("blocks left:", n)
            print("score:", get_score(prog.output))
    elif ball[0] == paddle[0]:
        prog.run(input=0, reset=False)
        n_prev = n
        n = count_blocks(prog.output)
        if n != n_prev:
            show_grid(prog.output)
            print("blocks left:", n)
            print("score:", get_score(prog.output))
    if n == 0:
        break

print("score:", get_score(prog.output))