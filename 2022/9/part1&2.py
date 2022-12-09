from AoC_tools import aoc22 as aoc

def move(d, pos_h):
    """move algorith for the head"""
    x1, y1 = pos_h
    if d == 'U':
        y1 += 1
    elif d == 'D':
        y1 -= 1
    elif d == 'L':
        x1 -= 1
    elif d == 'R':
        x1 += 1
    return (x1, y1)


def follow(pos_1, pos_2):
    """Move algorithm for any knot that follows the head.
    Pos_1 is the knot in front, pos_2 is the follower."""
    x1, y1 = pos_1
    x2, y2 = pos_2
    if abs(y1 - y2) == 2 and abs(x1 - x2) == 0:
        y2 += int((y1 - y2) / 2)
    elif abs(x1 - x2) == 2 and abs(y1 - y2) == 0:
        x2 += int((x1 - x2) / 2)
    elif abs(y1 - y2) == 2 and abs(x1 - x2) == 1:
        y2 += int((y1 - y2) / 2)
        x2 += (x1 - x2)
    elif abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
        x2 += int((x1 - x2) / 2)
        y2 += (y1 - y2)
    # only needed in part 2
    elif abs(x1 - x2) == 2 and abs(y1 - y2) == 2:
        x2 += int((x1 - x2) / 2)
        y2 += int((y1 - y2) / 2)
    return (x2, y2)


def run(tail_length):
    positions = [(0,0) for i in range(tail_length + 1)]
    covered = []
    for d in data:
        direction = d[0]
        steps = int(d[1])
        #print(f"moving {direction} {steps} steps")
        for i in range(steps):
            positions[0] = move(direction, positions[0])
            for i in range(1, len(positions)):
                positions[i] = follow(positions[i-1], positions[i])
            covered.append(positions[tail_length])
        # print(positions)
    return len(set(covered))


data = aoc.read_input("input.txt", "\n", " ")

# part 1
assert run(1) == 6011

# part 2
assert run(9) == 2419
