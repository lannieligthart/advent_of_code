import sys
sys.path.append("C:/Users/Admin/Documents/Code/advent_of_code/2019/5")
import IntCode as ic

code = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/9/input.txt')
prog = ic.Intcode(code)
print(prog.run(reset=False, debug=True, input=1))
