with open('input.txt') as f:
    data = f.read().split("\n")

print(data)

import pandas as pd
import itertools
import operator
import numpy as np

grid = [list(d) for d in data]
grid = pd.DataFrame(grid)
print(grid)

nrows = grid.shape[0]
ncols = grid.shape[1]

def center(asteroid, ref, reverse=False):
    row = ref[0]
    col = ref[1]
    if not reverse:
        a0 = asteroid[0] - row
        a1 = asteroid[1] - col
    else:
        a0 = asteroid[0] + row
        a1 = asteroid[1] + col
    return (a0, a1)


def find_observed(others):
    # find observable asteroids from the center of the grid (0,0)
    biggest = max(nrows, ncols)
    common_denominators = {}
    smallest_fractions = {}
    # ga alle asteroids langs
    for o in others:
        cd = []
        # en test door welke getallen (groter dan 0) zowel r als c deelbaar zijn, waarbij het maximale getal de grootste
        # dimensie van de grid is
        for i in range(1, biggest):
            if o[0] % i == 0 and o[1] % i == 0:
                cd.append(i)
        common_denominators[o] = cd
        # bepaal de kleinste fractie door door de grootste common denominator te delen
        max_cd = max(cd)
        x = int(o[0]/max_cd)
        y = int(o[1]/max_cd)
        sf = (x, y)
        smallest_fractions[o] = sf

    # als er nu twee in de lijst zitten die dezelfde kleinste fractie hebben, liggen ze onder dezelfde hoek vanaf (0,0)
    # gezien. Alleen de kleinste daarvan wordt gezien vanaf 0,0.
    # loop alle combi's langs om dat te bepalen.

    combos = list(itertools.combinations(smallest_fractions, 2))
    same_angle = []

    for c in combos:
        if smallest_fractions[c[0]] == smallest_fractions[c[1]]:
            #print(c)
            same_angle.append(c)

    observed_asteroids = others.copy()

    def remove_farthest(observed_asteroids, x1, x2):
        # do this only if they have the same sign (i.e. are on the same side of the asteroid)
        if np.sign(x1) == np.sign(x2) or (x1 == 0 and x2 == 0):
            # if first asteroid has a larger absolute coordinate than the second, keep the second, and vice versa
            if abs(x1) > abs(x2):
                observed_asteroids = [o for o in observed_asteroids if o != c[0]]
            elif abs(x1) < abs(x2):
                observed_asteroids = [o for o in observed_asteroids if o != c[1]]
        return observed_asteroids

    # first compare coordinates based on row number, delete the one with the highest row number.
    # then compare based on column numbers in case they are on the same row but different columns.
    for c in same_angle:
        observed_asteroids = remove_farthest(observed_asteroids, c[0][0], c[1][0])
        observed_asteroids = remove_farthest(observed_asteroids, c[0][1], c[1][1])

    return observed_asteroids


def find_best_asteroid(asteroids):
    n_obs = {}

    # loop door alle asteroids om te kijken hoeveel ze kunnen observeren
    for candidate in asteroids:
        others = [x for x in asteroids if x != candidate]
        # bepaal positie van alle asteroids ten opzichte van a
        centered_others = []
        for other in others:
            pos = center(other, candidate)
            centered_others.append(pos)

        # genereer lijst van alle asteroids die geobserveerd kunnen worden door a
        observed = find_observed(centered_others)
        # converteer de posities terug naar de werkelijke posities
        observed = [center(obs, candidate, reverse=True) for obs in observed]
        #print("from asteroid", candidate, "we can observe", (len(observed)), "others")
        n_obs[candidate] = len(observed)

    for key, value in n_obs.items():
        print(key, value)

    best_asteroid = max(n_obs.items(), key=operator.itemgetter(1))[0]
    n_observed = n_obs[best_asteroid]
    return (best_asteroid, n_observed)



def order_angles(observed):
    # sorteer ze per kwadrant
    q1 = []
    q2 = []
    q3 = []
    q4 = []
    for a in observed:
        row = a[0]
        col = a[1]
        if row < 0 and col >= 0:
            q1.append(a)
        elif row >= 0 and col>= 0:
            q2.append(a)
        elif row >= 0 and col< 0:
            q3.append(a)
        elif row < 0 and col < 0:
            q4.append(a)

    # alles schalen naar 1 col unit
    # daarna sorteren op rij units (ascending)
    def sort_quadrant(quad):
        angles = {}
        for ast in quad:
            if ast[1] != 0:
                angle = ast[0] / ast[1]
            elif ast[1] == 0:
                angle = -1000 # to avoid div/0 issues I picked an arbitrary large enough number so it ends up first in the sort order
            angles[ast] = angle
        sorted_angles = sorted(angles.items(), key=lambda x: x[1])
        sorted_angles = [x[0] for x in sorted_angles]
        print("q1 sorted:", sorted_angles)
        return sorted_angles

    sorted_asteroids = sort_quadrant(q1)
    sorted_asteroids.extend(sort_quadrant(q2))
    sorted_asteroids.extend(sort_quadrant(q3))
    sorted_asteroids.extend(sort_quadrant(q4))

    return sorted_asteroids

asteroids = []

for r in range(nrows):
    for c in range(ncols):
        if grid.loc[r,c] == '#':
            asteroids.append((r,c))

print(asteroids)

#for testinput
#cand = (13, 11)

#for real input
cand = (21, 20)

others = [x for x in asteroids if x != cand]
# bepaal positie van alle asteroids ten opzichte van a

obliteration_order = []

while len(others) > 0:
    centered_others = []
    for other in others:
        pos = center(other, cand)
        centered_others.append(pos)

    obs = find_observed(centered_others)
    obs_ordered = order_angles(obs)
    print(obs_ordered)
    obs_ordered = [center(x, cand, reverse=True) for x in obs_ordered]
    print(obs_ordered)
    for i in obs_ordered:
        others.remove(i)

    obliteration_order.extend(obs_ordered)

result = obliteration_order[199]
result = result[0] * 100 + result[1]
assert result==1919
