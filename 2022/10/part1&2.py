import AoC_tools.aoc22 as aoc

class Program(object):

    def __init__(self):
        self.cycle = 0
        self.x = 1
        self.values = dict()
        self.crt = ''  # index 0 of the crt string gets a space because this will not be used.

    @property
    def sprite(self):
        """Instruction says: "the X register sets the horizontal position of the middle of that sprite."
        This suggests that for the minimum value of x, the first pixel of the sprite is off-screen.
        However, because the X is one-based, it can never be smaller than 1 and for a value of 1, the sprite starts at
        index 0 of the CRT. Translated to the one-based indices of the value mapping, the sprite's positions are in
        fact [x, x+1, x+2]"""
        return list(range(self.x, self.x + 3))

    def noop(self):
        self.cycle += 1
        self.values[self.cycle] = self.x
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
        # here we do use zero-based indexing!
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
    result += i * program.values[i]

#assert result == 13140
assert result == 15260

# part 2
program.print_crt()

#assert program.crt == '##..##..##..##..##..##..##..##..##..##..###...###...###...###...###...###...###.####....####....####....####....####....#####.....#####.....#####.....#####.....######......######......######......###########.......#######.......#######.....'
assert program.crt == '###...##..#..#.####..##..#....#..#..##.##..#.#..#.#..#.#....#..#.#....#..#.#..###..#.#....####.###..#....#....#..#.#...####..#.##.#..#.#....#.##.#....#..#.#.####....#..#.#..#.#....#..#.#....#..#.#..#.#.....###.#..#.#.....###.####..##...###.'

# PGHFGLUG

