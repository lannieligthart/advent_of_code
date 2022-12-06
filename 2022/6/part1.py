with open("input.txt") as f:
    data = f.read()

def find_marker(data, n):
    for i in range(len(data)):
        str = data[i:i + n]
        if len(set(list(str))) == n:
            return i + n

assert find_marker(data, 4) == 1929