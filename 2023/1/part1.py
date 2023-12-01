with open("input.txt") as file:
    data = file.read().split("\n")

lines = []

for line in data:
    digits = ''
    for ch in line:
        if ch.isdigit():
            digits += ch
    lines.append(digits)

result = 0
for l in lines:
    result += int(l[0] + l[-1])

assert result == 53651