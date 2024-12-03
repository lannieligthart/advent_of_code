import re

infile = "input.txt"
#infile = "testinput.txt"

with open(infile) as f:
    data = f.read()

data = re.findall("mul\([0-9]+,[0-9]+\)", data)

total = 0

for d in data:
    d = d.replace("mul(", "")
    d = d.replace(")", "")
    d = d.split(",")
    total += int(d[0]) * int(d[1])

print(total)

if infile == "testinput.txt":
    assert total == 161
elif infile == "input.txt":
    assert total == 165225049