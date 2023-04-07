from AoC_tools import aoc22 as aoc

with open("input.txt") as file:
    data = file.read().split("\n")

data.sort()
aoc.lprint(data)

guards = dict()
asleep_times = []
wake_times = []
guard = None
for d in data:
    if "Guard" in d:
        if guard is not None:
            intervals = []
            for i in range(len(asleep_times)):
                intervals.append((asleep_times[i], wake_times[i]))
            if not int(guard) in guards:
                guards[int(guard)] = intervals
            else:
                guards[int(guard)].extend(intervals)
        guard = d.split("#")[1].split(" ")[0]
        asleep_times = []
        wake_times = []
    elif "asleep" in d:
        t1 = d.split(":")[1].split("]")[0]
        asleep_times.append(int(t1))
    elif "wakes" in d:
        t2 = d.split(":")[1].split("]")[0]
        wake_times.append(int(t2))

# TODO: de laatste gaat nu niet mee, dit moet netter
intervals = []
for i in range(len(asleep_times)):
    intervals.append((asleep_times[i], wake_times[i]))
if not int(guard) in guards:
    guards[int(guard)] = intervals
else:
    guards[int(guard)].extend(intervals)

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

max = [None, 0]

for key, value in guards.items():
    time_asleep = get_asleep_time(value)
    if time_asleep > max[1]:
        max = [key, time_asleep]

guard_most_asleep = max[0]
time_asleep = max[1]

#print(f"Guard most asleep: {guard_most_asleep}, Time asleep: {time_asleep}")

max_final = [None, None, 0]

for key, value in guards.items():
    minutes = dict()
    for minute in range(0, 60):
        minutes[minute] = 0
        minutes[minute] = times_asleep_during_minute(value, minute)

    max = [None, 0]

    for key2, value2 in minutes.items():
        if value2 > max[1]:
            max = [key2, value2]

    print(f"Minute guard {key} is most often asleep: {max[0]} ({max[1]} times)")
    if max[1] > max_final[2]:
        max_final = [key, max[0], max[1]]

print(max_final)
print(max_final[0] * max_final[1])

assert max_final[0] * max_final[1] == 7887