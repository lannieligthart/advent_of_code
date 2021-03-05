import unittest
import sys
sys.path.append("C:/Users/Admin/Documents/Code/advent_of_code/2019/5")
import IntCode as ic
import itertools


class TestOpcodes(unittest.TestCase):

    def test_day2_testinput2(self):
        code_day2 = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/5/testinput2.txt')
        day2 = ic.Intcode(code_day2)
        day2.run()
        self.assertEqual({0: 1101, 1: 100, 2: -1, 3: 4, 4: 99}, day2.code)

    def test_day5_testinput(self):
        testcode_day5 = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/5/testinput.txt')
        day5test = ic.Intcode(testcode_day5)
        self.assertEqual({0: 1002, 1: 4, 2: 3, 3: 4, 4: 33}, day5test.code)
        day5test.run()
        self.assertEqual({0: 1002, 1: 4, 2: 3, 3: 4, 4: 99}, day5test.code)

    def test_equals_8(self):
        self.code = ic.parse("3,9,8,9,10,9,4,9,99,-1,8")
        self.prog = ic.Intcode(self.code)
        self.assertEqual(self.prog.run(8, reset=True), 1)
        self.assertEqual(self.prog.run(7), 0)

    def test_less_than_8(self):
        self.code = ic.parse("3,9,7,9,10,9,4,9,99,-1,8")
        self.prog = ic.Intcode(self.code)
        self.assertEqual(self.prog.run(8, reset=True), 0)
        self.assertEqual(self.prog.run(7), 1)

    def test_equals_8_immediate_mode(self):
        self.code = ic.parse("3,3,1108,-1,8,3,4,3,99")
        self.prog = ic.Intcode(self.code)
        self.assertEqual(self.prog.run(8, reset=True), 1)
        self.assertEqual(self.prog.run(7), 0)

    def test_less_than_8_immediate_mode(self):
        self.code = ic.parse("3,3,1107,-1,8,3,4,3,99")
        self.prog = ic.Intcode(self.code)
        self.assertEqual(self.prog.run(8, reset=True), 0)
        self.assertEqual(self.prog.run(7), 1)

    def test_jump_zero_if_input_zero(self):
        self.code = ic.parse("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9")
        self.prog = ic.Intcode(self.code)
        self.assertEqual(self.prog.run(0, reset=True), 0)
        self.assertEqual(self.prog.run(3), 1)

    def test_jump_zero_if_input_zero_immediate(self):
        self.code = ic.parse("3,3,1105,-1,9,1101,0,0,12,4,12,99,1")
        self.prog = ic.Intcode(self.code)
        self.assertEqual(self.prog.run(0, reset=True), 0)
        self.assertEqual(self.prog.run(2323), 1)

    def test_longer_example_day5_2(self):
        #999 if value below 8, 1000 if equal to 8, 1001 if larger than 8
        self.code = ic.parse("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,"
                     "999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")
        self.prog = ic.Intcode(self.code)
        self.assertEqual(999, self.prog.run(7))
        self.assertEqual(1000, self.prog.run(8, reset=True))
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
        self.prog.add()
        self.assertEqual({0: 1, 1: 1, 2: 2, 3: 3, 4: 4, 5: 95, 6: -1}, self.prog.code)

    def test_add_immediate(self):
        self.code = ic.parse("1,97,2,6,4,95,-1")
        self.prog = ic.Intcode(self.code)
        self.prog.par1.value = 97
        self.prog.par2.value = 2
        self.prog.par3.value = 6
        self.prog.par1.mode = 1
        self.prog.par2.mode = 1
        self.prog.par3.mode = 1
        self.prog.add()
        self.assertEqual({0: 1, 1: 97, 2: 2, 3: 6, 4: 4, 5: 95, 6: 99}, self.prog.code)

    def test_day7_ex1(self):
        code = ic.parse("109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99")
        expected = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
        prog = ic.Intcode(code)
        for _ in range(len(code)):
            result = prog.run(reset=False, return_last=False)
        self.assertEqual(expected, result)

    def test_day7_ex2(self):
        code = ic.parse("1102,34915192,34915192,7,4,7,99,0")
        prog = ic.Intcode(code)
        self.assertEqual(1219070632396864, prog.run(reset=False))

    def test_day7_ex3(self):
        code = ic.parse("104,1125899906842624,99")
        prog = ic.Intcode(code)
        self.assertEqual(1125899906842624, prog.run(reset=False))

    def test_relative_mode(self):
        prog = ic.Intcode([109, -1, 204, 1, 99])
        self.assertEqual(109, prog.run())
        prog = ic.Intcode([109, 1, 9, 2, 204, -6, 99])
        self.assertEqual(204, prog.run())
        prog = ic.Intcode([109, 1, 109, 9, 204, -6, 99])
        self.assertEqual(204, prog.run())
        prog = ic.Intcode([109, 1, 209, -1, 204, -106, 99])
        self.assertEqual(204, prog.run())
        prog = ic.Intcode([109, 1, 3, 3, 204, 2, 99])
        self.assertEqual(66, prog.run(66))
        prog = ic.Intcode([109, 1, 203, 2, 204, 2, 99])
        self.assertEqual(66, prog.run(66))

    def test_day2_part1(self):
        code_day2 = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/2/input.txt')
        day2 = ic.Intcode(code_day2)
        day2.run(value1=12, value2=2, reset=False)
        self.assertEqual(day2.code[0], 3101878)

    def test_day2_part2(self):
        code_day2 = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/2/input.txt')
        day2 = ic.Intcode(code_day2)
        day2.run(value1=84, value2=44)
        self.assertEqual(19690720, day2.code[0])

    def test_day5_part1(self):
        code_day5 = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/5/input.txt')
        day5 = ic.Intcode(code_day5)
        while True:
            result = day5.run(input=1, reset=False, return_last=True)
            if result != 0:
                break
        self.assertEqual(result, 14155342)

    def test_day5_part2(self):
        code_day5 = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/5/input.txt')
        day5 = ic.Intcode(code_day5)
        result = day5.run(input=5, return_last=True)
        self.assertEqual(8684145, result)

    def test_day7_1_ex1(self):
        code = ic.parse('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0')
        seq = [4, 3, 2, 1, 0]
        amps = []
        input = 0
        for i in range(5):
            amps.append(ic.Intcode(code))
            # first provide the phase setting
            amps[i].run(seq[i], reset=False)
            # then provide input. The output will be the new input for the next round.
            input = amps[i].run(input, reset=False)
        self.assertEqual(43210, input)

    def test_day7_1_ex2(self):
        code = ic.parse('3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0')
        seq = [0,1,2,3,4]
        amps = []
        input = 0
        for i in range(5):
            amps.append(ic.Intcode(code))
            # first provide the phase setting
            amps[i].run(seq[i], reset=False)
            # then provide input. The output will be the new input for the next round.
            input = amps[i].run(input, reset=False)
        self.assertEqual(54321, input)

    def test_day7_1_ex3(self):
        code = ic.parse('3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0')
        seq = [1,0,4,3,2]
        amps = []
        input = 0
        for i in range(5):
            amps.append(ic.Intcode(code))
            # first provide the phase setting
            amps[i].run(seq[i], reset=False)
            # then provide input. The output will be the new input for the next round.
            input = amps[i].run(input, reset=False)
        self.assertEqual(65210, input)


    def test_day7_2_ex1(self):
        code = ic.parse('3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5')
        seq = [9,8,7,6,5]
        amps = []
        results = []
        input = 0
        # set up the amps and generate the first output signal
        for i in range(5):
            amps.append(ic.Intcode(code))
            amps[i].run(seq[i], reset=False, halt_on_output=True)
            input = amps[i].run(input, reset=False, halt_on_output=True)
        # use the last output signal as input and cycle through the set of amps
        while True:
            i += 1
            i = i % len(seq)
            input = amps[i].run(input, reset=False, halt_on_output=True)
            if i == 4 and input is not None:
                results.append(input)
            if i == 4 and amps[i].code[amps[i].pointer] == 99:
               break
        highest = max(results)
        self.assertEqual(139629729, highest)


    def test_day7_part1(self):
        code = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/7/input.txt')
        seq = list(itertools.permutations(range(5), 5))
        results = []
        for s in seq:
            amps = []
            input = 0
            for i in range(5):
                amps.append(ic.Intcode(code))
                amps[i].run(s[i], reset=False)
                input = amps[i].run(input, reset=False)
            results.append(input)
        result = max(results)
        self.assertEqual(result, 366376)

    def test_day7_part2(self):
        code = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/7/input.txt')
        seqs = list(itertools.permutations(range(5, 10), 5))
        max_results = []
        for seq in seqs:
            results = []
            amps = []
            input = 0
            # set up the amps and generate the first output signal
            for i in range(5):
                amps.append(ic.Intcode(code))
                amps[i].run(seq[i], reset=False, halt_on_output=True)
                input = amps[i].run(input, reset=False, halt_on_output=True)
            # use the last output signal as input and cycle through the set of amps
            while True:
                i += 1
                i = i % len(seq)
                input = amps[i].run(input, reset=False, halt_on_output=True)
                if i == 4 and input is not None:
                    results.append(input)
                if i == 4 and amps[i].code[amps[i].pointer] == 99:
                   break
            max_results.append(max(results))
        self.assertEqual(21596786, max(max_results))




if __name__ == '__main__':
    unittest.main()