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

# find the guard that spends the most minutes asleep

# keep track of the max encountered so far
max = [None, 0]

# loop through all the guards
for key, value in guards.items():
    time_asleep = get_asleep_time(value)
    # if higher than max recorded, replace max
    if time_asleep > max[1]:
        max = [key, time_asleep]

# write results to readable variable name
guard_most_asleep = max[0]
time_asleep = max[1]

print(f"Guard most asleep: {guard_most_asleep}, Time asleep: {time_asleep}")

# loop through all minutes (0-59) to see how many times the guard was asleep during each minute, and store in a dict
minutes = dict()
for minute in range(0, 60):
    minutes[minute] = 0
    minutes[minute] = times_asleep_during_minute(guards[guard_most_asleep], minute)

# get the minute the guard was most often asleep
max = [None, 0]
for key, value in minutes.items():
    if value > max[1]:
        max = [key, value]

print(f"Minute guard is most often asleep: {max[0]} ({max[1]} times)")

print(guard_most_asleep * max[0])

assert guard_most_asleep * max[0] == 95199