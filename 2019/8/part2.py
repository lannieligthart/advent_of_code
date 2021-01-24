with open('input.txt') as f:
    data = f.read()

# cols = 2
# rows = 2
cols = 25
rows = 6

layers = []
pos = 0
for c in range(int(len(data)/rows/cols)):
    layer = []
    for r in range(rows):
        layer.append(data[pos:pos+cols])
        pos += cols
    layers.append(layer)

# loop through all all rows and all columns
# start with first layer, if not a 2, write and continue

image = [ [] for _ in range(rows) ]
for r in range(rows):
    for c in range(cols):
        for l in layers:
            if l[r][c] == '1':
                image[r] += l[r][c]
                break
            elif l[r][c] == '0':
                image[r] += ' '
                break
for i in image:
    print("".join(i))
