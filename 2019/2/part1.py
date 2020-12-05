with open('C:/Users/Admin/Documents/Code/advent_of_code/2019/2/input.txt') as f:
    data = f.read().split(",")

for i in range(len(data)):
    data[i] = int(data[i])

# reset
data[1] = 12
data[2] = 2

print(data)
# 0 - opcode (1 = add, 2 = multiply, 99 = stop)
# 1 - pos int1
# 2 - pos int2
# 3 - position to store result

def add_ints(ints, data):
    sum = data[ints[1]] + data[ints[2]]
    data[ints[3]] = sum
    print("inserted", sum, "at position", ints[3])

def multiply_ints(ints, data):
    product = data[ints[1]] * data[ints[2]]
    data[ints[3]] = product
    print("inserted", product, "at position", ints[3])

pos = 0

while True:
    ints = data[pos:pos+4]

    if ints[0] == 99:
        break
    elif ints[0] == 1:
        add_ints(ints, data)
    elif ints[0] == 2:
        multiply_ints(ints, data)
    else:
        print("invalid intcode!")
        break
    pos += 4
    print(data)


