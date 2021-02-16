import unittest
import sys
sys.path.append("C:/Users/Admin/Documents/Code/advent_of_code/2019/5")
import IntCode as ic

class TestOpcodes(unittest.TestCase):

    def test_day2_part1(self):
        code_day2 = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/2/input.txt')
        day2 = ic.Intcode(code_day2)
        result = day2.run(value1=12, value2=2)
        self.assertEqual(result, 3101878)

    def test_day2_testinput2(self):
        code_day2 = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/5/testinput2.txt')
        day2 = ic.Intcode(code_day2)
        day2.run()
        self.assertEqual(day2.code, [1101, 100, -1, 4, 99])

    def test_day5_testinput(self):
        testcode_day5 = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/5/testinput.txt')
        day5test = ic.Intcode(testcode_day5)
        self.assertEqual(day5test.code, [1002, 4, 3, 4, 33])
        day5test.run()
        self.assertEqual(day5test.code, [1002, 4, 3, 4, 99])



    def test_equals_8(self):
        self.code = ic.parse("3,9,8,9,10,9,4,9,99,-1,8")
        self.prog = ic.Intcode(self.code)
        self.assertEqual(self.prog.run(8), 1)
        self.assertEqual(self.prog.run(7), 0)

    def test_less_than_8(self):
        self.code = ic.parse("3,9,7,9,10,9,4,9,99,-1,8")
        self.prog = ic.Intcode(self.code)
        self.assertEqual(self.prog.run(8), 0)
        self.assertEqual(self.prog.run(7), 1)

    def test_equals_8_immediate_mode(self):
        self.code = ic.parse("3,3,1108,-1,8,3,4,3,99")
        self.prog = ic.Intcode(self.code)
        self.assertEqual(self.prog.run(8), 1)
        self.assertEqual(self.prog.run(7), 0)

    def test_less_than_8_immediate_mode(self):
        self.code = ic.parse("3,3,1107,-1,8,3,4,3,99")
        self.prog = ic.Intcode(self.code)
        self.assertEqual(self.prog.run(8), 0)
        self.assertEqual(self.prog.run(7), 1)

    def test_jump_zero_if_input_zero(self):
        self.code = ic.parse("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9")
        self.prog = ic.Intcode(self.code)
        self.assertEqual(self.prog.run(0, debug=True), 0)
        self.assertEqual(self.prog.run(3, debug=True), 1)

    def test_jump_zero_if_input_zero_immediate(self):
        self.code = ic.parse("3,3,1105,-1,9,1101,0,0,12,4,12,99,1")
        self.prog = ic.Intcode(self.code)
        self.assertEqual(self.prog.run(0), 0)
        self.assertEqual(self.prog.run(2323), 1)

    def test_longer_example_day5_2(self):
        #999 if value below 8, 1000 if equal to 8, 1001 if larger than 8
        self.code = ic.parse("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,"
                     "999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")
        self.prog = ic.Intcode(self.code)
        self.assertEqual(999, self.prog.run(7, debug=True))
        self.assertEqual(1000, self.prog.run(8))
        self.assertEqual(1001, self.prog.run(9))

    def test_add_position(self):
        self.code = ic.parse("1,1,2,-1,4,95,-1")
        self.prog = ic.Intcode(self.code)
        self.prog.par1.value = 1
        self.prog.par2.value = 2
        self.prog.par3.value = 3
        self.prog.par1.mode = 0
        self.prog.par2.mode = 0
        self.prog.par3.mode = 0
        self.prog.add(debug=False)
        self.assertEqual(self.prog.code, [1, 1, 2, 3, 4, 95, -1])

    def test_add_immediate(self):
        self.code = ic.parse("1,97,2,6,4,95,-1")
        self.prog = ic.Intcode(self.code)
        self.prog.par1.value = 97
        self.prog.par2.value = 2
        self.prog.par3.value = 6
        self.prog.par1.mode = 1
        self.prog.par2.mode = 1
        self.prog.par3.mode = 1
        self.prog.add(debug=False)
        self.assertEqual(self.prog.code, [1, 97, 2, 6, 4, 95, 99])

    def test_day2_part1(self):
        code_day2 = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/2/input.txt')
        day2 = ic.Intcode(code_day2)
        self.assertEqual(3101878, day2.run(value1=12, value2=2))

    def test_day2_part2(self):
        code_day2 = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/2/input.txt')
        day2 = ic.Intcode(code_day2)
        self.assertEqual(19690720, day2.run(value1=84, value2=44))

    def test_day5_part1(self):
        code_day5 = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/5/input.txt')
        day5 = ic.Intcode(code_day5)
        result = 0
        while result == 0:
            result = day5.run(input=1, reset=False)
        print(result)
        self.assertEqual(result, 14155342)

    def test_day5_part3(self):
        code_day5 = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/5/input.txt')
        day5 = ic.Intcode(code_day5)
        result = day5.run(input=5)
        self.assertEqual(8684145, result)



if __name__ == '__main__':
    unittest.main()