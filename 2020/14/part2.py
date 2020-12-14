import itertools

with open('input.txt') as f:
    data = f.read().split("\n")

for i in range(len(data)):
    data[i] = data[i].split(" = ")

#print(data)

# memory is a dictionary of positions and values
memory = {}

def apply_bitmask(value, mask):
    value_new = []
    for i in range(len(mask)):
        # X wordt X
        if mask[i] == 'X':
            value_new.append(mask[i])
        # 0 doet niks
        elif mask[i] == '0':
            value_new.append(value[i])
        # 1 wordt 1
        elif mask[i] == '1':
            value_new.append(mask[i])
    value_new = "".join(value_new)
    return value_new

def int2bin(str):
    value = int(str)
    value = bin(value)[2:].zfill(36)
    return value

def get_bitset(n):
    return list(itertools.product([0, 1], repeat=n))


def generate_options(value):
    # genereer de adressen gebaseerd op X-en in de value na toepassing mask
    nx = value.count('X')
    bitset = get_bitset(nx)
    #print(bitset)
    new_values = []
    # loop mask door en vul eerste optie in
    for option in range(pow(2, nx)):
        tmp = []
        x = 0
        for i in range(len(value)):
            if value[i] != 'X':
                tmp.append(value[i])
            elif value[i] == 'X':
                tmp.append(bitset[option][x])
                x += 1
        for i in range(len(tmp)):
            tmp[i] = str(tmp[i])
        new_value = "".join(tmp)
        new_values.append(int(new_value,2))
    return new_values


mask = None
location = None
value = None
for i in range(len(data)):
    if data[i][0] == 'mask':
        # this becomes the mask for the next several values
        mask = data[i][1]
    elif data[i][0].startswith('mem'):
        # format correctly
        target = data[i][0].replace("mem[", "")
        target = target.replace("]", "")
        # target is waar de nieuwe waarden naartoe geschreven moeten worden.
        target = int(target)
        # get the target (not the value this time!) and apply the bitmask to it
        target = int2bin(target)
        # apply the mask
        masked_value = apply_bitmask(target, mask)
        # get the different targets resulting from the mask, in int format
        targets = generate_options(masked_value)
        # get the value to be written to these targets
        value = int(data[i][1])
        for t in targets:
            memory[t] = value
#print(memory)


assert (sum(memory.values())) == 4197941339968

