from AoC_tools import aoc24 as aoc
import itertools

s = aoc.start()
#infile = "testinput.txt"
infile = "input.txt"

with open(infile) as f:
    data = f.read().split("\n")

data = [d.split() for d in data]

eq = dict()

for d in data:
    eq[int(d[0].replace(":", ""))] = d[1:]

def try_combo(combo, numbers):
    answer = numbers[0]
    for i in range(len(numbers) - 1):
        eq = str(answer) + combo[i] + numbers[i+1]
        #print(eq)
        answer = eval(eq)
    return answer

total = 0

for key, value in eq.items():
    combos = itertools.product(["*", "+"], repeat=len(value) - 1)
    answers = []
    for combo in combos:
        answer = try_combo(combo, value)
        if answer == key:
            total += key
            break


aoc.check_result(infile, total, 3749, 932137732557, s)