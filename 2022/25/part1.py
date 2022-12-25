from AoC_tools.aoc22 import *

data = read_input("input.txt")

data = list(map(list, data))

for d in data:
    for i in range(len(d)):
        d[i] = d[i].replace("-", "-1")
        d[i] = d[i].replace("=", "-2")
        d[i] = int(d[i])

def decode(snafu_number):
    snafu_number.reverse()
    total = 0
    for i in range(len(snafu_number)):
        total +=  snafu_number[i] * 5**i
    return total

def encode(decimal_number):
    wb = {-2: '=', -1: '-', 0: '0', 1: '1', 2: '2'}
    # bepaal welke macht van 5 groter is dan number
    i = 0
    while True:
        if 5 ** i > decimal_number:
            break
        i += 1
    snafu_tmp = []
    for j in range(i):
        for delta in [-2, -1, 0, 1, 2]:
            if (decimal_number - delta*5**j) % 5**(j+1) == 0:
                snafu_tmp.append(delta)
                decimal_number -= 5**j * delta
                break
    snafu_tmp.reverse()
    snafu = ''
    for s in snafu_tmp:
        snafu += wb[s]
    return snafu


total = 0
for sn in data:
    total += decode(sn)

assert total == 28127432121050
snafu = encode(total)
assert snafu == "122-2=200-0111--=200"
