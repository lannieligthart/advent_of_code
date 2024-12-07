infile = "testinput.txt"
#infile = "input.txt"

with open(infile) as f:
    data = f.readlines()

print(f"rows:{len(data)}")
print(f"cols:{len(data[0])}")

for c in range(len(data)-1):
    for r in range(len(data[0])-1):
        if data[r][c] == "^":
            curpos = (r,c)

print(f"start position: {curpos}")

directions = ["N", "E", "S", "W"]

move_dir = {"N": (-1, 0),
            "S": (1, 0),
            "E": (0, 1),
            "W": (0, -1)}

visited = [curpos]
direction = 0

r, c = curpos

while True:
    old = (r, c)
    r += move_dir[directions[direction]][0]
    c += move_dir[directions[direction]][1]
    # if the guard has left the map, stop
    if r < 0 or r >= len(data) or c < 0 or c >= len(data[0]):
        break
    if data[r][c] != "#":
        visited.append((r,c))
        #print(r, c)
        #print(visited)
    elif data[r][c] == "#":
        r, c = old
        direction += 1
        direction = direction % 4
        print(f"current position: ({r, c})")
        print(f"turning {directions[direction]}")

print(visited)
visited = list(set(visited))
print(len(visited))


#4434 klopt niet
#4433 is het juiste antwoord?

