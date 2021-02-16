import sys
sys.path.append("C:/Users/Admin/Documents/Code/advent_of_code/2019/5")
import IntCode as ic

code_day2 = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/2/input.txt')
day2 = ic.Intcode(code_day2)
self.assertEqual(3101878, day2.run(value1=12, value2=2))
