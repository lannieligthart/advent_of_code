with open("input.txt") as file:
    data = file.read().split("\n")

durations = list(map(int, data[0].split()[1:]))
records = list(map(int, data[1].split()[1:]))

def optimize(duration, record):
    durations = []
    for i in range(duration + 1):
        distance = i * (duration - i)
        if distance > record:
            durations.append(i)
    return durations

result = []
for i in range(len(durations)):
    result.append(len(optimize(durations[i], records[i])))

product = result[0]
for i in range(1, len(result)):
    product = product * result[i]

assert product == 4403592