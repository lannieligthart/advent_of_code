import sys
sys.path.append("C:/Users/Admin/Documents/Code/advent_of_code/2019/5")
import IntCode as ic

# EXAMPLES
#
# code = ic.parse('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0')
# seq1 = [4, 3, 2, 1, 0]
#
# code = ic.parse('3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0')
# seq1 = [0,1,2,3,4]

# REAL INPUT

code = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/7/input.txt')

import itertools

seq = list(itertools.permutations(range(5), 5))

results = []

for s in seq:
    amps = []
    inp2 = 0
    for i in range(5):
        inp1 = s[i]
        print("*** adding new amp to the set")
        amps.append(ic.Intcode(code))
        print("*** run amp ", i, "with input", inp1, inp2)
        inp2 = amps[i].run([inp1, inp2], reset=False, debug=False)
    results.append(inp2)

print(max(results))





