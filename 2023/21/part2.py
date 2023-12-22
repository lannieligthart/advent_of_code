from AoC_tools import aoc23 as aoc
from AoC_tools import aoc22 as aoc22

start = aoc22.start()


def get_nb(pos):
    r, c = pos
    return [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]


def get_nb_and_grids(pos):
    r, c, rg, cg = pos
    nb = get_nb((r, c))
    result = []
    for n in nb:
        rn, cn = n
        rgnew, cgnew = rg, cg
        if rn > r_max:
            rn = 0
            rgnew = rg + 1
        if cn > c_max:
            cn = 0
            cgnew = cg + 1
        if rn < 0:
            rn = r_max
            rgnew = rg - 1
        if cn < 0:
            cn = c_max
            cgnew = cg - 1
        result.append((rn, cn, rgnew, cgnew))
    return result


with open("input.txt") as file:
    data = file.read()

grid = aoc.Matrix.read(data)
n_rows = grid.dim[0]
n_cols = grid.dim[1]
r_max = n_rows - 1
c_max = n_cols - 1


for key, value in grid.values.items():
    if value == 'S':
        start_pos = key
grid.pos = (start_pos)

start_pos = (start_pos[0], start_pos[1], 0, 0)  # start pos, grid pos

points = [(start_pos)]
new_nb = set()
rounds = 270  # at least twice the period is needed here
results = []

for i in range(rounds):
    nb = []
    while len(points) > 0:
        nb.extend(get_nb_and_grids(points.pop()))
    for n in nb:
        if grid.values[(n[0], n[1])] != "#":
            new_nb.add(n)
    points = new_nb
    results.append(len(new_nb))
    if i % 100 == 0:
        print(i)
    if i == rounds - 1:
        result = len(new_nb)
    new_nb = set()


period = 131  # figured this out by hand but should really code it

deltas = [results[i] - results[i-1] for i in range(1, len(results))]
betas = [deltas[i] - deltas[i-period] for i in range(period, len(results)-1)]

deltas.insert(0, None)
for i in range(period + 1):
    betas.insert(0, None)

print(f"at step {rounds}:")
print("n_nb:", results[-1])
print("delta:", deltas[-1])
print("beta:", betas[-1])
print("phase:", rounds % period)

step = rounds
while step < 26501365:
    phase = step % period
    betas.append(betas[step - period])
    deltas.append(deltas[step - period] + betas[-1])
    results.append(results[-1] + deltas[-1])
    step += 1

print("at step 26501365:")
print("n_nb:", results[-1])
print("delta:", deltas[-1])
print("beta:", betas[-1])
print("phase:", phase)


assert results[-1] == 616951804315987

end = aoc22.end(start)