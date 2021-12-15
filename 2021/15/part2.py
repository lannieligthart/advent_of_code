import AoC_tools.aoc_tools as aoc

data = aoc.lines2lol("input.txt", numeric=True)

# Iterative function to find the minimum cost to traverse from the
# first cell to the last cell of a matrix, using Dijkstra's algorithm because part 2 includes other
# moves than just right and down. Therefore the part 1 script doesn't work here.
def findMinCost(cost):
    # R × C matrix
    (R, C) = (len(cost), len(cost[0]))

    # T[r][c] maintains the minimum cost to reach cell (i, j) from cell (0, 0)
    T = [[10000 for x in range(C)] for y in range(R)]
    queue = [(r, c) for r in range(R) for c in range(C)]
    # first element has 0 cost
    T[0][0] = 0
    for item in queue:
        # items to evaluate:
        r, c = item
        nb = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        nb = [(r, c) for r, c in nb if r >= 0 and c >= 0]
        for nr, nc in nb:
            # neighbour krijgt de cumulatieve cost van het huidige item plus z'n eigen cost, tenzij z'n actuele
            # cumulatieve cost (waarde in T) lager is dan wat hij nu zou krijgen.
            try:
                new_cost = T[r][c] + cost[nr][nc]
                if T[nr][nc] > new_cost:
                    T[nr][nc] = new_cost
                    queue.append((nr, nc))
            except IndexError:
                pass
    return T[R - 1][C - 1]

def expand_matrix(data, dim, round):
    for i in range(len(data)):
        for j in range(dim):
            newval = (data[i][j] + round)
            if newval >= 10:
                newval = newval - 9
            data[i].append(newval)
    for i in range(dim):
        newrow = []
        for x in data[i]:
            newval = x + round
            if newval >= 10:
                newval = newval - 9
            newrow.append(newval)
        data.append(newrow)
    return(data)

dim = len(data[0])

for round in range(1, 5):
    data = expand_matrix(data, dim=dim, round=round)

aoc.lprint(data)

min_cost = findMinCost(data)
print("The minimum cost is", min_cost)
asser min_cost == 2868
