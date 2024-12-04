#infile = "testinput.txt"
infile = "input.txt"

with open(infile) as f:
    data = f.read().split("\n")

print(data)

total = 0

# test alle richtingen.
def horizontal(data):
    total = 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            try:
                word = ''
                word += data[r][c]
                word += data[r][c+1]
                word += data[r][c+2]
                word += data[r][c+3]
                #print(word)
                if word == "XMAS" and len(data) > r >= 0 and len(data) > c+3 >= 0:
                    print(r, c)
                    total += 1
            except IndexError:
                pass
    for r in range(len(data)):
        for c in range(len(data[0])):
            try:
                word = ''
                word += data[r][c]
                word += data[r][c-1]
                word += data[r][c-2]
                word += data[r][c-3]
                #print(word)
                if word == "XMAS" and len(data) > r >= 0 and len(data) > c-3 >= 0:
                    print(r, c)
                    total += 1
            except IndexError:
                pass
    print(f"horizontal: {total}")
    return total


def vertical(data):
    total = 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            try:
                word = ''
                word += data[r][c]
                word += data[r+1][c]
                word += data[r+2][c]
                word += data[r+3][c]
                #print(word)
                if word == "XMAS" and len(data) > r+3 >= 0 and len(data) > c >= 0:
                    print(r, c)
                    total += 1
            except IndexError:
                pass
    for r in range(len(data)):
        for c in range(len(data[0])):
            try:
                word = ''
                word += data[r][c]
                word += data[r-1][c]
                word += data[r-2][c]
                word += data[r-3][c]
                #print(word)
                if word == "XMAS" and len(data) > r-3 >= 0 and len(data) > c >= 0:
                    print(r, c)
                    total += 1
            except IndexError:
                pass
    print(f"vertical: {total}")
    return total

def diagonal(data):
    total = 0
    print("rechts omlaag")
    for r in range(len(data)):
        for c in range(len(data[0])):
            try:
                word = ''
                word += data[r][c]
                word += data[r+1][c+1]
                word += data[r+2][c+2]
                word += data[r+3][c+3]
                #print(word)
                if word == "XMAS" and len(data) > r+3 >= 0 and len(data) > c+3 >= 0:
                    print(r, c)
                    total += 1
            except IndexError:
                pass
    print("links omhoog")
    for r in range(len(data)):
        for c in range(len(data[0])):
            try:
                word = ''
                word += data[r][c]
                word += data[r-1][c-1]
                word += data[r-2][c-2]
                word += data[r-3][c-3]
                #print(word)
                if word == "XMAS" and len(data) > r-3 >= 0 and len(data) > c-3 >= 0:
                    print(r, c)
                    total += 1
            except IndexError:
                pass

    print("links omlaag")
    for r in range(len(data)):
        for c in range(len(data[0])):
            try:
                word = ''
                word += data[r][c]
                word += data[r+1][c-1]
                word += data[r+2][c-2]
                word += data[r+3][c-3]
                #print(word)
                if word == "XMAS" and len(data) > r+3 >= 0 and len(data) > c-3 >= 0:
                    print(r, c)
                    total += 1
            except IndexError:
                pass
    print("rechts omhoog")
    for r in range(len(data)):
        for c in range(len(data[0])):
            try:
                word = ''
                word += data[r][c]
                word += data[r-1][c+1]
                word += data[r-2][c+2]
                word += data[r-3][c+3]
                #print(word)
                if word == "XMAS" and len(data) >= r-3 >= 0 and len(data) > c+3 >= 0:
                    print(r, c)
                    total += 1
            except IndexError:
                pass
    print(f"diagonal: {total}")
    return total

total += horizontal(data)
total += vertical(data)
total += diagonal(data)
print(total)

