with open("input.txt") as file:
    data = file.read().split("\n")

# parse input to a list of tuples
data = [tuple(map(int, d.split("x"))) for d in data]

def get_surface(dim):
    l, w, h = dim
    sizes = [2 * l * w, 2 * w * h, 2 * h * l]
    return int(sum(sizes) + 0.5 * min(sizes))

total = 0
for d in data:
    total += get_surface(d)

assert total == 1598415

