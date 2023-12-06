import re
with open("input.txt") as file:
    data = file.read().split("\n")

duration = re.sub("\s+", "", data[0])
duration = int(duration.replace("Time:", ""))
record = re.sub("\s+", "" , data[1])
record = int(record.replace("Distance:", ""))

def optimize(duration, record):
    durations = []
    # start at beginning and record only the first one that breaks the record
    i = 0
    while True:
        distance = i * (duration - i)
        if distance > record:
            durations.append(i)
            break
        i += 1
    i = duration
    # now start at the end and do the same
    while True:
        distance = i * (duration - i)
        if distance > record:
            durations.append(i)
            break
        i -= 1
    return durations

result = optimize(duration, record)
result = (result[1]) - (result[0] - 1)

assert result == 38017587

