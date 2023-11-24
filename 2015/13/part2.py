from itertools import permutations

with open("input.txt") as file:
    data = file.read().split("\n")

data = [d.replace("would ", "") for d in data]
data = [d.replace("happiness units by sitting next to ", "") for d in data]
data = [d.replace(".", "") for d in data]
data = [d.split() for d in data]

overview = dict()
guests = set()

for d in data:
    guests.add(d[0])
    guests.add(d[3])
    if d[1] == "gain":
        overview[(d[0], d[3])] = int(d[2])
    elif d[1] == "lose":
        overview[(d[0], d[3])] = -int(d[2])

# add myself
guests.add("Lannie")

for g in guests:
    overview["Lannie", g] = 0
    overview[g, "Lannie"] = 0

# obtain all possible seating arrangements
seating_arrangements = permutations(guests)

def get_happiness(seating_arrangement):
    happiness = 0
    for i in range(len(seating_arrangement)):
        guest = seating_arrangement[i]
        nb1 = seating_arrangement[i - 1]
        nb2 = seating_arrangement[(i + 1) % len(guests)]
        happiness += overview[(guest, nb1)]
        happiness += overview[(guest, nb2)]
    return happiness

results = dict()

for s in seating_arrangements:
    results[s] = get_happiness(s)

assert max(results.values()) == 640