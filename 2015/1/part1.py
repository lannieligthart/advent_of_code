with open("input.txt") as file:
    data = file.read()

def get_floor_part1(data):
    floor = 0
    for char in data:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
    return floor

def get_floor_part2(data):
    floor = 0
    for pos, char in enumerate(data):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        if floor == -1:
            return pos + 1
    return floor


assert get_floor_part1(data) == 280
assert get_floor_part2(data) == 1797