import sys
sys.path.append("C:/Users/Admin/Documents/Code/advent_of_code/2019/5")
import IntCode as ic


#
# code = ic.parse("109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99")
# prog = ic.Intcode(code)
# for _ in range(len(code)):
#     prog.run(reset=False, debug=False)
# print(prog.run(reset=False))
#
#
#
#
# code = ic.parse("1102,34915192,34915192,7,4,7,99,0")
# prog = ic.Intcode(code)
# print(prog.run(reset=False))
#
#
#
# code = ic.parse("104,1125899906842624,99")
# prog = ic.Intcode(code)
# print(prog.run(reset=False))


code = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/9/input.txt')
prog = ic.Intcode(code)
print(prog.run(reset=False, debug=True, input=1))

#203 too low