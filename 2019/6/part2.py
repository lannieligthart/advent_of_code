with open('input.txt') as f:
    data = f.read().split("\n")

data = [d.split(")") for d in data]

obs = {}
for i in range(len(data)):
    obs[data[i][1]] = data[i][0]

for key, value in obs.items():
    print(key, "orbits around", value)

# keys are orbiting objects, values the orbited objects
def track(value, obs):
    transfers = []
    while True:
        transfers.append(value)
        try:
            key = value
            value = obs[key]
        except KeyError:
            break
    return transfers

key = 'YOU'
value = obs[key]
tr_you = track(value, obs)
key = 'SAN'
value = obs[key]
tr_san = track(value, obs)

for x in tr_you:
    if x in tr_san:
        first_common = x
        break

result = tr_you.index(first_common) + tr_san.index(first_common)
print(result)
assert result == 499