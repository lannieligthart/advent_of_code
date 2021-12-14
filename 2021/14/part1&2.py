with open("input.txt") as f:
    polymer, instructions = f.read().split("\n\n")

instructions = instructions.split("\n")

for i in range(len(instructions)):
    instructions[i] = instructions[i].split(" -> ")

tmp = {}
for i in instructions:
    tmp[i[0]] = i[1]
instructions = tmp

def count_elements(polymer):
    # takes a dictionary of pairs and returns the counts for each element
    elements = {}
    for pair in polymer:
        el1, el2 = pair[0], pair[1]
        for el in [el1, el2]:
            if el not in elements:
                elements[el] = polymer[pair]
            else:
                elements[el] += polymer[pair]
    elements['N'] += 1
    elements['B'] += 1
    elements = {key: int(value/2) for key, value in elements.items()}
    return elements


def step(polymer, instructions):
    newpol = {}
    for pair in polymer.keys():
        newpair1, newpair2 = pair[0] + instructions[pair], instructions[pair] + pair[1]
        for np in [newpair1, newpair2]:
            if np not in newpol:
                newpol[np] = polymer[pair]
            else:
                newpol[np] += polymer[pair]
    polymer = newpol
    return polymer

tmp = {}
for i in range(len(polymer)-1):
    if polymer[i:i+2] not in tmp:
        tmp[polymer[i:i+2]] = 1
    else:
        tmp[polymer[i:i+2]] += 1

# part 1:
polymer = tmp
for s in range(10):
    polymer = step(polymer, instructions)

count = (count_elements(polymer))
result = max(count.values()) - min(count.values())
assert result == 2745

# part 2:
polymer = tmp
for s in range(40):
    polymer = step(polymer, instructions)

count = (count_elements(polymer))
result = max(count.values()) - min(count.values())
assert result == 3420801168962
