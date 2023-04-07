import AoC_tools.aoc_tools as aoc

data = aoc.read_input("input.txt", "\n")

data = list(map(int, data))

def get_repeated_freq(data):
    count = 0
    d = {0: 1}
    idx = 0
    while True:
        count += data[idx]
        if not count in d:
            d[count] = 1
            idx += 1
            idx = idx % len(data)
        else:
            d[count] += 1
            if d[count] == 2:
                return count


assert get_repeated_freq(data) == 70357

