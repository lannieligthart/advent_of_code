with open('input.txt') as f:
    data = f.read()

# cols = 3
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

def count_digits(digit, layer):
    count = 0
    for pixel in layer:
        count += pixel.count(digit)
    return count

counts = []
for l in layers:
    counts.append(count_digits('0', l))

idx = counts.index(min(counts))
selected = layers[idx]
ones = count_digits('1', selected)
twos = count_digits('2', selected)
result = ones * twos
print(result)
assert result == 1965