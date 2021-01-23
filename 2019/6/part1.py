with open('input.txt') as f:
    data = f.read().split("\n")

data = [d.split(")") for d in data]
print(data)

obs = {}
for i in range(len(data)):
    obs[data[i][1]] = data[i][0]

for key, value in obs.items():
    print(key, "orbits around", value)

# keys are orbiting objects, values the orbited objects
count = 0
for key, value in obs.items():
    while True:
        count += 1
        try:
            key = value
            value = obs[key]
        except KeyError:
            break

print(count)
assert count == 253104