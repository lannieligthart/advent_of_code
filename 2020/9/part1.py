import itertools

with open('input.txt') as f:
    data = f.read().split("\n")

for i in range(len(data)):
    data[i] = int(data[i])
print(data)

preamble_size = 5

def get_sums(data, pos, preamble_size):
    sums = []
    sets = []
    preamble = data[pos:pos+preamble_size]
    for subset in itertools.combinations(preamble,2 ):
        sets.append(subset)
        sums.append(sum(subset))
    return sums

def get_odd_one_out(data, preamble_size):
    numbers = data[preamble_size:]
    pos = 0
    for n in numbers:
        sums = get_sums(data, pos, preamble_size)
        if not n in sums:
            return(n)
        pos += 1

print(get_odd_one_out(data, preamble_size=25))

