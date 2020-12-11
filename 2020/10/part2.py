with open('input.txt') as f:
    data = f.read().split("\n")

data = [int(d) for d in data]
data.sort()
print(data)

jolts = [0]
jolts.extend(data)
jolts.append(data[-1] + 3)

print(jolts)

difs = []
for i in range(1, len(jolts)):
    difs.append(jolts[i] - jolts[i-1])

print(difs)

# er zijn alleen verschillen van 1 of 3.
# bij een verschil van 3 weet je dat er maar 1 optie is.
# bij een verschil van 1 hangt het af van hoeveel enen er achter elkaar staan.
# bepaal de lengtes van de blokken met enen.
lengths = []

start = None
end = None
if difs[0] == 1:
    start = 0
for i in range(len(difs)-1):
    if difs[i] == 3 and difs[i+1] == 1:
        start = i+1
    if difs[i] == 1 and difs[i+1] == 3:
        end = i+1
    if start is not None and end is not None:
        lengths.append(end-start)
        start = None
        end = None

print(lengths)
# max length is 4

product = 1
for i in lengths:
    if i == 2:
        product *= 2
    elif i == 3:
        product *= 4
    elif i == 4:
        product *= 7

print(product)