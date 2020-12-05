with open('input.txt') as f:
    text = f.read().splitlines()

lines = []
lines = [x.split(" ") for x in text]
pw_correct = 0

for i in lines:
    char = i[1].split(":")[0]
    n = i[2].count(char)
    min = int(i[0].split("-")[0])
    max = int(i[0].split("-")[1])
    if n >= min and n <= max:
        pw_correct += 1

print(pw_correct)



