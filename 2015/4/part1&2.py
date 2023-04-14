import hashlib

# part 1

i = 1

while True:
    input = 'yzbqklnj' + str(i)
    s = input.encode()
    s = hashlib.md5(s)
    if s.hexdigest().startswith("00000"):
        print(s.hexdigest(), i)
        break
    i += 1

assert i == 282749

# for part 2, continue from the current value of i

while True:
    input = 'yzbqklnj' + str(i)
    s = input.encode()
    s = hashlib.md5(s)
    if s.hexdigest().startswith("000000"):
        print(s.hexdigest(), i)
        break
    i += 1

assert i == 9962624