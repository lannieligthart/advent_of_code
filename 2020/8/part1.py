with open('input.txt') as f:
    code = f.read().split("\n")

for i in range(len(code)):
    code[i] = code[i].split(" ")
    code[i][1] = int(code[i][1])

#print(code)

pos = 0
acc_value = 0

class boot_code(object):

    def __init__(self, code):
        self.pos = 0
        self.acc_value = 0
        self.code = code
        self.track = [None] * len(self.code)
        self.step = 0

    def nop(self):
        self.track[self.pos] = self.step
        self.pos += 1
        self.step += 1

    def acc(self, value):
        self.track[self.pos] = self.step
        self.acc_value += value
        self.pos += 1
        self.step += 1

    def jmp(self, value):
        self.track[self.pos] = self.step
        self.pos += value
        self.step += 1

    def run(self):
        print(self.pos)
        while self.track[self.pos] is None:
            if self.code[self.pos][0] == 'nop':
                self.nop()
            elif self.code[self.pos][0] == 'acc':
                self.acc(value=self.code[self.pos][1])
            elif self.code[self.pos][0] == 'jmp':
                self.jmp(value=self.code[self.pos][1])
            #print(self.pos)
            print(self.acc_value)
        return(self.acc_value)

prog = boot_code(code)
print(prog.run())
#assert prog.run() == 5