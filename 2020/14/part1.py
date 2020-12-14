with open('testinput.txt') as f:
    data = f.read().split("\n")

for i in range(len(data)):
    data[i] = data[i].split(" = ")

print(data)

# memory is a dictionary of positions and values
memory = {}

def apply_bitmask(value, mask):
    value_new = []
    for i in range(len(mask)):
        if mask[i] == 'X':
            value_new.append(value[i])
        elif mask[i] != "X":
            value_new.append(mask[i])
    value_new = "".join(value_new)
    return value_new

def int2bin(str):
    value = int(str)
    value = bin(value)[2:].zfill(36)
    return value

mask = None
location = None
value = None
for i in range(len(data)):
    if data[i][0] == 'mask':
        mask = data[i][1]
    elif data[i][0].startswith('mem'):
        target = data[i][0].replace("mem[", "")
        target = target.replace("]", "")
        target = int(target)
        value = int2bin(data[i][1])
        memory[target] = int(apply_bitmask(value, mask), 2)

print(memory)
print(sum(memory.values()))

assert sum(memory.values()) == 15172047086292

#value = "000000000000000000000000000000001011"
#mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
# print(int(apply_bitmask(value, mask), 2))
#
# value = "000000000000000000000000000001100101"
# print(int(apply_bitmask(value, mask), 2))
#
# value = "000000000000000000000000000000000000"
# print(int(apply_bitmask(value, mask), 2))
#

