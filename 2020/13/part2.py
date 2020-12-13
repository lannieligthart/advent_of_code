# Didn't solve this one alone...

with open('input.txt') as f:
    data = f.read().split("\n")

numbers = data[1].split(",")
buses = []
for i in range(len(numbers)):
    if numbers[i] != 'x':
        buses.append(int(numbers[i]))
    elif numbers[i] == 'x':
        buses.append(None)

# the intervals we are looking for in the sequence of numbers we need
offsets = []
offset = 0
for i in range(0, len(buses)):
    if buses[i] is not None:
        offsets.append(offset)
        offset += 1
    elif buses[i] is None:
        offset += 1

buses = [b for b in buses if b is not None]

print("buses:", buses)
print("offsets:", offsets)

class Bus(object):

    def __init__(self, period, offset):
        self.period = period
        self.offset = offset % period # aanpassing voor het geval de offset groter is dan de period

    def __str__(self):
        return "period: " + str(self.period) + "; offset: " + str(self.offset)

    def merge(self, other):
        offset = None
        n = self.offset
        while True:
            if (other.period - n % other.period) == other.offset:
                if offset is None:
                    offset = n
                else:
                    return Bus(n - offset, offset)
            n += self.period

i = 0
bus1 = Bus(buses[i], offsets[i])
for i in range(len(buses)-1):
    bus2 = Bus(buses[i+1], offsets[i+1])
    bus1 = bus1.merge(bus2)
    print(bus1)


assert bus1.offset == 471793476184394