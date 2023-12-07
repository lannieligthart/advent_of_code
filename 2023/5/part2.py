with open("input.txt") as file:
    data = file.read().split("\n\n")

seeds = list(map(int,data[0].split()[1:]))
seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_ranges.append((seeds[i], seeds[i] + seeds[i+1]))

conversions = dict()

for d in data[1:]:
    d = d.split(" map:\n")
    conversion_ranges = []
    lines = d[1].split("\n")
    for line in lines:
        dest, start, r = list(map(int, line.split()))
        conversion_ranges.append((start, start + r, dest - start))
    conversions[d[0]] = conversion_ranges

def find_cut_points(conversion_ranges):
    # voor de input range, kijk welke cut points er zijn.
    # als een cut point binnen de range ligt, knip de range in stukken.
    cut_points = set()
    for cr in conversion_ranges:
        cut_points.add(cr[0])
        cut_points.add(cr[1])
    # sorteer ze
    cut_points = list(cut_points)
    cut_points.sort()
    return cut_points

def cut_range(input_range, cut_points):
    start, stop = input_range
    # bepaal welke cut points in deze range liggen
    cp = [start]
    for p in cut_points:
        if p > start and p < stop:
            cp.append(p)
    cp.append(stop)
    cut_ranges = []
    for i in range(0, len(cp)-1):
        cut_ranges.append((cp[i], cp[i+1]))
    return cut_ranges

def modify_range(r, conversion_ranges):
    for c in conversion_ranges:
        mod = c[2]
        if r[0] >= c[0] and r[1] <= c[1]:
            return (r[0] + mod, r[1] + mod)
    # if it's in none of the conversion ranges, return the unmodified range
    return r

for conversion, conversion_ranges in conversions.items():
    cut_ranges = []
    cp = find_cut_points(conversion_ranges)
    for s in seed_ranges:
        cut_ranges.extend(cut_range(s, cp))
    converted_ranges = []
    for r in cut_ranges:
        converted_ranges.append(modify_range(r, conversion_ranges))
    seed_ranges = converted_ranges

lowest = min([s[0] for s in seed_ranges])

assert lowest = 78775051

