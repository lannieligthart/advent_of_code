import itertools
import numpy as np
import copy

with open('testinput.txt') as f:
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
        #print(c[0], c[1])
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


# def compare(start_positions, moons_position, n):
#     same = [[None, None, None], [None, None, None], [None, None, None], [None, None, None]]
#     for i in range(len(start_positions)):
#         # if start_positions[i] == moons_position[i]:
#         #     same[i] = n
#         for j in range(len(start_positions[i])):
#             if start_positions[i][j] == moons_position[i][j]:
#                 same[i][j] = n
#     return same

def compare(start_positions, start_velocities, moons_position, moons_velocity, n):
    same = [None, None, None, None]
    for i in range(len(start_positions)):
        if start_positions[i] == moons_position[i] and start_velocities[i] == moons_velocity[i]:
            same[i] = n
            print(moons_position)
            print(n)
    return same


start_positions = copy.deepcopy(moons_position)
start_velocities = copy.deepcopy(moons_velocity)

n = 0
periods = [[], [], [], []]

while True:
    n += 1
    moons_position, moons_velocity = time_step(moons_position, moons_velocity)
    #print(moons_position, moons_velocity)
    same = compare(start_positions, start_velocities, moons_position, moons_velocity, n)
    for i in range(len(same)):
        #for j in range(len(same[i])):
            # if same[i][j] is not None and periods[i][j] is None:
            #     periods[i][j] = n
        if same[i] is not None:
            periods[i].append(same[i])
            print(periods)
#    if not None in periods[0] and not None in periods[1] and not None in periods[2]:
    p_len = [len(periods[i]) for i in range(len(periods))]
    if min(p_len) > 0:
       break

# all_periods = periods[0]
# all_periods.extend(periods[1])
# all_periods.extend(periods[2])
# all_periods.extend(periods[3])
# print(all_periods)

#
# def merge(p1, p2):
#     if p1 > p2:
#         largest = p1
#         smallest = p2
#     elif p1 < p2:
#         largest = p1
#         smallest = p2
#     increment = largest
#     while True:
#         if largest % smallest == 0:
#             return largest
#         largest += increment
#
#
# #period = merge(all_periods[0], all_periods[1])
# period = merge(periods[0], periods[1])
#
# for i in range(2, len(periods)):
#     period = merge(period, periods[i])
#     print(period)


# [924, 617, 2772, 924]