with open('input.txt') as f:
    data = f.read().split("\n")

print(data)

import pandas as pd
import itertools
import operator

grid = [list(d) for d in data]
grid = pd.DataFrame(grid)
print(grid)

nrows = grid.shape[0]
ncols = grid.shape[1]

def center(asteroid, rc):
    row = rc[0]
    col = rc[1]
    a0 = asteroid[0] - row
    a1 = asteroid[1] - col
    return (a0, a1)


def decenter(asteroid, rc):
    row = rc[0]
    col = rc[1]
    a0 = asteroid[0] + row
    a1 = asteroid[1] + col
    return (a0, a1)


def find_observed(others):
    # find observable asteroids from the center of the grid (0,0)
    #others = [a for a in centered_asteroids if a != (0,0)]

    # grootst mogelijke coordinaat
    biggest = max(nrows, ncols)
    common_denominators = {}
    smallest_fractions = {}
    # ga alle asteroids langs
    for o in others:
        cd = []
        # en test door welke getallen (groter dan 0) zowel r als c deelbaar zijn, waarbij het maximale getal de grootste dimensie van
        # de grid is
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

    for c in same_angle:
        if c[0][0] > c[1][0]:
            observed_asteroids = [o for o in observed_asteroids if o != c[0]]
        elif c[0][0] < c[1][0]:
            observed_asteroids = [o for o in observed_asteroids if o != c[1]]
        elif c[0][0] > c[0][1]:
            observed_asteroids = [o for o in observed_asteroids if o != c[0]]
        elif c[0][0] < c[0][1]:
            observed_asteroids = [o for o in observed_asteroids if o != c[1]]

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
        observed = [decenter(obs, candidate) for obs in observed]
        #print("from asteroid", candidate, "we can observe", (len(observed)), "others")
        n_obs[candidate] = len(observed)

    for key, value in n_obs.items():
        print(key, value)

    best_asteroid = max(n_obs.items(), key=operator.itemgetter(1))[0]
    n_observed = n_obs[best_asteroid]
    return (best_asteroid, n_observed)

asteroids = []

for r in range(nrows):
    for c in range(ncols):
        if grid.loc[r,c] == '#':
            asteroids.append((r,c))

print(asteroids)

best = find_best_asteroid(asteroids)

print(best)

assert best[1] == 247
# 21, 20 (r, c)

# (20, 21) 247

# note that I use r, c, AoC uses c, r.