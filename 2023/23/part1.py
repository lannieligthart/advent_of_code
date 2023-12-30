from AoC_tools import aoc22 as aoc

start = aoc.start()


def in_data(pos, data):
    r, c = pos
    if 0 <= r < len(data) and c >= 0 and c < len(data[0]):
        return True
    else:
        return False


def find_longest_path(data):
    queue = [[(0, 1)]]
    while len(queue) > 0:
        path = queue.pop(0)
        r, c = path[-1]
        n = (r-1, c)
        e = (r, c+1)
        s = (r+1, c)
        w = (r, c-1)
        nb = [n, e, s, w]
        allowed = ["^", ">", "v", "<"]
        options = []
        for i, n in enumerate(nb):
            if in_data(n, data) and (data[n[0]][n[1]] == "." or data[n[0]][n[1]] == allowed[i]) and n not in path:
                options.append(n)
        newpaths = []
        for o in options:
            newpath = path.copy()
            newpath.append(o)
            newpaths.append(newpath)
        for np in newpaths:
            if np[-1] == finish:
                completed.append(np)
            else:
                queue.append(np)


with open("input.txt") as file:
    data = file.read().split("\n")

finish = (len(data)-1, len(data[0])-2)
completed = []
find_longest_path(data)

assert max([len(p) for p in completed]) - 1 == 2210

aoc.end(start)