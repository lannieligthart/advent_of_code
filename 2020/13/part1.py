with open('input.txt') as f:
    data = f.read().split("\n")

print(data)
cur_time = int(data[0])
numbers = data[1].split(",")
buses = []
for i in range(len(numbers)):
    if numbers[i] != 'x':
        buses.append(int(numbers[i]))

print(buses)

close_departures = []
for b in buses:
    time = b
    while True:
        time += b
        if time >= cur_time:
            close_departures.append(time)
            break

print(close_departures)
difs = [i - cur_time for i in close_departures]
print(difs)
min_dif = min(difs)
bus_index = difs.index(min_dif)
print(bus_index)
best_bus = buses[bus_index]
print(best_bus)

print(best_bus * difs[bus_index])