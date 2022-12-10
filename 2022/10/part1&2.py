import AoC_tools.aoc22 as aoc

class Program(object):

    def __init__(self):
        self.cycle = 0
        self.x = 1
        self.cycles = [0]
        self.values = [1]
        self.crt = ''

    @property
    def sprite(self):
        return list(range(self.x, self.x + 3))

    def noop(self):
        self.cycle += 1
        self.cycles.append(self.cycle)
        self.values.append(self.x)
        self.draw()

    def addx(self, n):
        for i in range(2):
            self.noop()
        self.x += n

    def draw(self):
        if self.cycle % 40 in self.sprite:
            self.crt += "#"
        else:
            self.crt += "."

    def print_crt(self):
        start = 0
        end = 39
        # replace # and . by characters that make the result more readable
        crt = self.crt.replace("#", "█").replace(".", "░")
        while end <= len(crt):
            print(crt[start:end])
            start += 40
            end += 40

    def run(self, data):
        for d in data:
            if d == 'noop':
                self.noop()
            else:
                n = int(d.split()[1])
                self.addx(n)


#data = aoc.read_input("testinput.txt")
data = aoc.read_input("input.txt")

program = Program()
program.run(data)

# part 1
result = 0
for i in [20, 60, 100, 140, 180, 220]:
    result += program.cycles[i] * program.values[i]

#assert result == 13140
assert result == 15260

# part 2
program.print_crt()

#assert program.crt == '##..##..##..##..##..##..##..##..##..##..###...###...###...###...###...###...###.####....####....####....####....####....#####.....#####.....#####.....#####.....######......######......######......###########.......#######.......#######.....'
assert program.crt == '###...##..#..#.####..##..#....#..#..##.##..#.#..#.#..#.#....#..#.#....#..#.#..###..#.#....####.###..#....#....#..#.#...####..#.##.#..#.#....#.##.#....#..#.#.####....#..#.#..#.#....#..#.#....#..#.#..#.#.....###.#..#.#.....###.####..##...###.'

# PGHFGLUG

