
with open("input.txt") as file:
    data = file.read()

data = data.split(",")

def hash(data):
    value = 0
    for char in data:
        value += ord(char)
        value *= 17
        value = value % 256
    return value

assert sum([hash(d) for d in data]) == 517965
