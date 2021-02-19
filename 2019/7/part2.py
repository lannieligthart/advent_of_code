import sys
sys.path.append("C:/Users/Admin/Documents/Code/advent_of_code/2019/5")
import IntCode as ic

# EXAMPLES

code = ic.parse('3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5')
seq = [9, 8, 7, 6, 5]

code = ic.parse('3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,'
                '0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10')
seq = [9,7,8,5,6]

results = []
amps = []
inp2 = 0

for i in range(5):
    #print("*** Amp", i)
    inp1 = seq[i]
    amps.append(ic.Intcode(code))
    #print("*** called with input", inp1, inp2)
    inp2 = amps[i].run([inp1, inp2], reset=False)
    #print("Amp", i, "'s code:", amps[i].code)

while True:
    i += 1
    i = i % len(seq)
    #print("*** Amp", i)
    inp1 = seq[i]
    #print("*** called with input", inp2)
    inp2 = amps[i].run([inp2], reset=False)
    #print("pointer position:", amps[i].pointer)
    #print("Amp", i, "'s code:", amps[i].code)
    if i == 4:
        #print("Amp E's output:",  inp2)
        results.append(inp2)
    if i == 4 and amps[i].code[amps[i].pointer] == 99:
        break

print(max(results))

# REAL INPUT

code = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/7/input.txt')

import itertools

seqs = list(itertools.permutations(range(5,10), 5))

max_results = []

for seq in seqs:
    results = []
    amps = []
    inp2 = 0
    for i in range(5):
        inp1 = seq[i]
        amps.append(ic.Intcode(code))
        print("inp1:", inp1, "inp2:", inp2)
        inp2 = amps[i].run([inp1, inp2], reset=False, debug=False)
        print("*** OUTPUT:", inp2)
    while True:
        i += 1
        i = i % len(seq)
        inp1 = seq[i]
        print("inp2:", inp2)
        inp2 = amps[i].run([inp2], reset=False, debug=False)
        print("*** OUTPUT:", inp2)
        if i == 4:
            results.append(inp2)
        if i == 4 and amps[i].code[amps[i].pointer] == 99:
            break
    max_results.append(max(results))

print(max(max_results))

assert max(max_results) == 21596786