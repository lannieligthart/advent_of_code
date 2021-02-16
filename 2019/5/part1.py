import sys
sys.path.append("C:/Users/Admin/Documents/Code/advent_of_code/2019/5")
import IntCode as ic

code_day5 = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/5/input.txt')
day5 = ic.Intcode(code_day5)
result = 0
while result == 0:
    result = day5.run(input=1, reset=False)
print(result)
assert result == 14155342