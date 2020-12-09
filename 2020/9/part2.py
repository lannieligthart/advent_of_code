import itertools

with open('input.txt') as f:
    data = f.read().split("\n")

for i in range(len(data)):
    data[i] = int(data[i])

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

def find_contiguous_sequence(data, invalid_number):
    pos = 0
    while True:
        seq_sum = 0
        sequence = []
        numbers = data[pos:]
        for n in numbers:
            sequence.append(n)
            seq_sum += n
            if seq_sum > invalid_number:
                pos += 1
                break
            elif seq_sum == invalid_number:
                print(sequence)
                return max(sequence) + min(sequence)


preamble_size = 25
invalid_number = get_odd_one_out(data, preamble_size)
assert invalid_number == 400480901
assert find_contiguous_sequence(data, invalid_number) == 67587168