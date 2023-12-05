with open("testinput.txt") as file:
    data = file.read().split("\n\n")

seeds = list(map(int,data[0].split()[1:]))
data = data[1:]
maps = dict()

print(seeds)
print(data)

for d in data:
    d = d.split(" map:\n")
    src = d[0].split("-")[0]
    dest = d[0].split("-")[2]
    print(dest, src)
    maps[src, dest] = []
    lines = d[1].split("\n")
    for line in lines:
        d, s, r = list(map(int, line.split()))
        print(s, d, r)
        rng = range(s, s + r)
        delta = d - s
        maps[src, dest].append((rng, delta))

print(f"from source to destination:")
for key, value in maps.items():
    print(key, value)

def translate(number, src, dest):
    # if the seed is in any of the ranges in the dictionary, apply a translation.
    # if not, leave unaltered.
    ranges = maps[(src, dest)]
    for r in ranges:
        if number in r[0]:
            number += r[1]
            return number
    return number

from_to = maps.keys()
locations = []
range1 = range(seeds[0], seeds[0] + seeds[1])
range2 = range(seeds[2], seeds[2] + seeds[3])

for location in range1:
    for key in from_to:
        src, dest = key
        location = (translate(location, src, dest))
    locations.append(location)
    # als heel range1 valt binnen 1 van de ranges in de dictionary voor deze src/dest hoef ik alleen de eerste van de range te bepalen.



for location in range2:
    for x in from_to:
        src, dest = x
        location = (translate(location, src, dest))
    locations.append(location)

print(min(locations))
