import sys
sys.path.append("C:/Users/Admin/Documents/Code/advent_of_code/2019/13")
sys.path.append("C:/Users/Admin/Documents/Code/advent_of_code/AoC_tools")
import IntCode as ic
from aoc_tools import display_grid
import time

code = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/13/input.txt')
# play for free
code[0] = 2
prog = ic.Intcode(code)

def read_instructions(instructions, get_tiles=True):
    tiles = {}
    pos = 0
    while pos < len(instructions):
        x = instructions[pos]
        y = instructions[pos + 1]
        tile_id = instructions[pos + 2]
        if tile_id == 4:
            ballx = x
        elif tile_id == 3:
            paddlex = x
        elif x == -1:
            score = tile_id
        if not x == -1 and get_tiles:
            tiles[(x, y)] = tile_id
        pos += 3
    return (ballx, paddlex, score, tiles)

def show_grid(tiles):
    lookup_table = {0: ' ', 1: 'W', 2: 'B', 3: '-', 4: 'O'}
    display_grid(tiles, lookup_table)

def count_blocks(tiles):
    block_tiles = [key for key, value in tiles.items() if value == 2]
    return len(block_tiles)

startTime = time.time()

prog.run(reset=False)
ballx, paddlex, score, tiles = read_instructions(prog.output, get_tiles=False)

while True:
    if ballx < paddlex:
        output = prog.run(input=-1, reset=False)
    elif ballx > paddlex:
        output = prog.run(input=1, reset=False)
    elif ballx == paddlex:
        output = prog.run(input=0, reset=False)
    old_score = score
    ballx, paddlex, score, tiles = read_instructions(prog.output, get_tiles=False)
    if score != old_score:
        ballx, paddlex, score, tiles = read_instructions(prog.output, get_tiles=True)
        #show_grid(tiles)
        n = count_blocks(tiles)
        print("blocks left:", n)
        #print("score:", score)
        if n == 0:
            break

print("score:", score)

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))


