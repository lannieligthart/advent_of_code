from collections import defaultdict

with open("input.txt") as file:
    data = file.read().split("\n")

data.sort()

guards = defaultdict()
asleep_times = []
wake_times = []
guard = None
for d in data:
    if "Guard" in d:
        guard = int(d.split("#")[1].split(" ")[0])
        if guard not in guards:
            guards[guard] = []
    elif "asleep" in d:
        t1 = d.split(":")[1].split("]")[0]
    elif "wakes" in d:
        t2 = d.split(":")[1].split("]")[0]
        guards[guard].append((int(t1), int(t2)))

for key, value in guards.items():
    print(key, value)

def get_asleep_time(intervals):
    time = 0
    for i in range(len(intervals)):
        time += intervals[i][1] - intervals[i][0]
    return time

def times_asleep_during_minute(intervals, minute):
    count = 0
    for i in range(len(intervals)):
        if minute >= intervals[i][0] and minute < intervals[i][1]:
            count += 1
    return count

max_guard = [None, None, 0]

# loop through all guards and make a count for how many times they are asleep each minute
for key, value in guards.items():
    minutes = dict()
    for minute in range(0, 60):
        minutes[minute] = 0
        minutes[minute] = times_asleep_during_minute(value, minute)

    # find the minute most often asleep
    max_minute = [None, 0]

    # check if this number exceeds the previously recorded max
    for key2, value2 in minutes.items():
        if value2 > max_minute[1]:
            max_minute = [key2, value2]

    # check if the max minutes for this guard exceeds the previously recorded max
    if max_minute[1] > max_guard[2]:
        max_guard = [key, max_minute[0], max_minute[1]]

print(f"Minute guard {max_guard[0]} is most often asleep: {max_guard[1]} ({max_guard[2]} times)")

assert max_guard[0] * max_guard[1] == 7887