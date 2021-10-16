import sys
sys.path.append("C:/Users/Admin/SURFdrive/Code/advent_of_code/2019/5")
import IntCode as ic

code = ic.parse_code('C:/Users/Admin/SURFdrive/Code/advent_of_code/2019/13/input.txt')
prog = ic.Intcode(code)

instructions = prog.run_to_end(reset=False)
print(instructions)

tiles = {}
pos = 0
while pos < len(instructions):
    x = instructions[pos]
    y = instructions[pos + 1]
    tile_id = instructions[pos + 2]
    tiles[(x, y)] = tile_id
    pos += 3

block_tiles = [key for key, value in tiles.items() if value == 2]
print(len(block_tiles))
print(block_tiles)

assert len(block_tiles) == 239
