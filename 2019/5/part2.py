import sys
sys.path.append("C:/Users/Admin/Documents/Code/advent_of_code/2019/5")
import IntCode as ic

code_day5 = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/5/input.txt')
day5 = ic.Intcode(code_day5)
result = day5.run(input=5)
print(result)
assert 8684145 == result