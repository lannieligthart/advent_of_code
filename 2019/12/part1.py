import itertools
import numpy as np

with open('input.txt') as f:
    data = f.read().split("\n")

moons_position = []
moons_velocity = []

for d in data:
    d = d.replace(">", "")
    d = d.replace("<x=", "")
    d = d.replace("y=", "")
    d = d.replace("z=", "")
    d = d.split(",")
    d = [int(x) for x in d]
    moons_position.append(d)
    moons_velocity.append([0, 0, 0])
print(moons_position)
print(moons_velocity)

def apply_gravity(pos1, pos2, vel1, vel2):
    for i in range(len(pos1)):
        if pos1[i] > pos2[i]:
            vel1[i] -= 1
            vel2[i] += 1
        elif pos1[i] < pos2[i]:
            vel1[i] += 1
            vel2[i] -= 1
    return (vel1, vel2)

def time_step(moons_position, moons_velocity):
    combos = list(itertools.combinations([0, 1, 2, 3], 2))
    for c in combos:
        m1 = c[0]
        m2 = c[1]
        print(c[0], c[1])
        moons_velocity[m1],  moons_velocity[m2] = apply_gravity(moons_position[m1], moons_position[m2], moons_velocity[m1], moons_velocity[m2])
    moons_position = np.array(moons_position) + np.array(moons_velocity)
    moons_position = [list(x) for x in moons_position]
    return (moons_position, moons_velocity)


def get_energy(moons_position, moons_velocity):
    pot = []
    kin = []
    for p in moons_position:
        p = [abs(x) for x in p]
        pot.append(sum(p))
    for v in moons_velocity:
        v = [abs(x) for x in v]
        kin.append(sum(v))
    tot = []
    for i in range(len(pot)):
        tot.append(pot[i] * kin[i])
    return sum(tot)


for _ in range(1000):
    moons_position, moons_velocity = time_step(moons_position, moons_velocity)
    print(moons_position, moons_velocity)

assert get_energy(moons_position, moons_velocity) == 7179

