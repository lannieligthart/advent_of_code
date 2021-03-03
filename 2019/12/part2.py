import itertools
import numpy as np
import copy

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


def compare(start_positions, start_velocities, moons_position, moons_velocity, n):
    same = [None, None, None]
    spos_x = [x[0] for x in start_positions]
    spos_y = [x[1] for x in start_positions]
    spos_z = [x[2] for x in start_positions]
    svel_x = [x[0] for x in start_velocities]
    svel_y = [x[1] for x in start_velocities]
    svel_z = [x[2] for x in start_velocities]
    pos_x = [x[0] for x in moons_position]
    pos_y = [x[1] for x in moons_position]
    pos_z = [x[2] for x in moons_position]
    vel_x = [x[0] for x in moons_velocity]
    vel_y = [x[1] for x in moons_velocity]
    vel_z = [x[2] for x in moons_velocity]
    if spos_x == pos_x and svel_x == vel_x:
        same[0] = n
    if spos_y == pos_y and svel_y == vel_y:
        same[1] = n
    if spos_z == pos_z and svel_z == vel_z:
        same[2] = n
    return same

start_positions = copy.deepcopy(moons_position)
start_velocities = copy.deepcopy(moons_velocity)

n = 0
periods = [[],[],[]]

while True:
    n += 1
    moons_position, moons_velocity = time_step(moons_position, moons_velocity)
    same = compare(start_positions, start_velocities, moons_position, moons_velocity, n)
    for i in range(len(same)):
        if same[i] is not None:
            periods[i].append(same[i])
            print(periods)

    p_len = []
    for i in range(len(periods)):
        p_len.append(len(periods[i]))
    if min(p_len) > 0:
       break

def merge(p1, p2):
    if p1 == p2:
        return p1
    elif p1 > p2:
        largest = p1
        smallest = p2
    elif p1 < p2:
        largest = p1
        smallest = p2
    increment = largest
    while True:
        if largest % smallest == 0:
            return largest
        largest += increment


def combine(moon_periods):
    moon_periods = sorted(moon_periods)
    numbers = moon_periods
    n1 = numbers[0]
    numbers = numbers[1:]
    while len(numbers) > 0:
        n1 = merge(n1, numbers[0])
        numbers = numbers[1:]
    return n1

# bepaal de periode voor elk van de coordinaten (voor alle manen tegelijk)
moon_periods = []
for i in range(len(periods)):
    moon_periods.append(periods[i][0])
print(moon_periods)

merged = []

print(merged)
merged = combine(moon_periods)

print(merged)



