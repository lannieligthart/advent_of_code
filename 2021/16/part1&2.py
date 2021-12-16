class Message(object):

    def __init__(self, msg):
        self.msg = self.hex2bin(msg)
        self.pointer = 0
        self.pv_sum = 0

    @staticmethod
    def hex2bin(txt):
        bin = ''
        for i in range(len(txt)):
            bin += str("{0:04b}".format(int(txt[i], 16)))
            i += 1
        return bin

    @staticmethod
    def bin2dec(txt):
        return int(txt, 2)

    def read(self):
        # first read packet version and type ID. Based on the type ID, choose a way to read further.
        typeid = self.read_header()
        if typeid == 4:
            number = self.read_literal()
        elif typeid != 4:
            number = self.read_operator(typeid)
        return number

    def read_header(self):
        pversion = self.bin2dec(self.msg[self.pointer:self.pointer + 3])
        self.pv_sum += pversion
        self.pointer += 3
        typeid = self.bin2dec(self.msg[self.pointer:self.pointer + 3])
        self.pointer += 3
        return typeid

    def read_literal(self):
        lastornot = int(self.msg[self.pointer])
        self.pointer += 1
        number = self.msg[self.pointer:self.pointer + 4]
        self.pointer += 4
        if lastornot == 0:
            number = self.bin2dec(number)
            return number
        while not lastornot == 0:
            lastornot = self.bin2dec(self.msg[self.pointer])
            number += self.msg[self.pointer + 1: self.pointer + 5]
            self.pointer += 5
        number = self.bin2dec(number)
        return number

    def read_operator(self, typeid):
        # this is the body of operator, the header has already been read.
        # Ltype specifies how the length/number of subpackets should be read.
        ltypeid = int(self.msg[self.pointer])
        self.pointer += 1
        numbers = []
        if ltypeid == 0:
            # 15 bits indicating total length of subpackets
            len_subp = self.bin2dec(self.msg[self.pointer:self.pointer + 15])
            self.pointer += 15
            end = self.pointer + len_subp
            #print("Total length of subpackets:", len_subp)
            while not self.pointer == end:
                numbers.append(self.read())
        elif ltypeid == 1:
            # 11 bits indicating N subpackets.
            n_subp = self.bin2dec(self.msg[self.pointer:self.pointer + 11])
            self.pointer += 11
            #print("N subpackets:", n_subp)
            i = 0
            while not i == n_subp:
                numbers.append(self.read())
                i += 1
        if typeid == 0:
            return sum(numbers)
        elif typeid == 1:
            p = 1
            for n in numbers:
                p = n * p
            return p
        elif typeid == 2:
            return min(numbers)
        elif typeid == 3:
            return max(numbers)
        elif typeid == 5:
            if numbers[0] > numbers[1]:
                return 1
            else:
                return 0
        elif typeid == 6:
            if numbers[0] < numbers[1]:
                return 1
            else:
                return 0
        elif typeid == 7:
            if numbers[0] == numbers[1]:
                return 1
            else:
                return 0

# test examples

msg = Message("C200B40A82")
assert msg.read() == 3

msg = Message("04005AC33890")
assert msg.read() == 54

msg = Message("880086C3E88112")
assert msg.read() == 7

msg = Message("CE00C43D881120")
assert msg.read() == 9

msg = Message("D8005AC2A8F0")
assert msg.read() == 1

msg = Message("F600BC2D8F")
assert msg.read() == 0

msg = Message("9C005AC2F8F0")
assert msg.read() == 0

msg = Message("9C0141080250320F1802104A08")
assert msg.read() == 1



with open("input.txt") as f:
    msg = f.read()
msg = Message(msg)
result = msg.read()

# part 1:
assert msg.pv_sum == 971

# part 2:
assert result == 831996589851

