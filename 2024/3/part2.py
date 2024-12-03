import re

infile = "input.txt"
#infile = "testinput.txt"

with open(infile) as f:
    data = f.read()

regex1 = "mul\([0-9]+,[0-9]+\)"
regex2 = "do\(\)"
regex3 = "don't\(\)"

data = re.findall("|".join([regex1, regex2, regex3]), data)
print(data)

remove = []
disabled = False

for i in range(len(data)):
    if "don't()" in data[i]:
        disabled = True
        remove.append(i)
    elif "do()" in data[i]:
        disabled = False
        remove.append(i)
    elif disabled:
        remove.append(i)

data = [data[i] for i in range(len(data)) if not i in remove]

total = 0

for d in data:
    d = d.replace("mul(", "")
    d = d.replace(")", "")
    d = d.split(",")
    total += int(d[0]) * int(d[1])

print(total)

if infile == "testinput.txt":
    assert total == 48
elif infile == "input.txt":
    assert total == 108830766