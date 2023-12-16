from AoC_tools import aoc22 as aoc

start = aoc.start()

# get all combinations
import itertools

with open("input.txt") as file:
    data = file.read().split("\n")


# per group, figure out where it might go.
def check_fit(length, string, pos):
    fit = True
    # als op een van de beoogde posities een . staat, past het niet
    if "." in string[pos:pos + length]:
        fit = False
    if pos > 0 and string[pos - 1] == "#":
        fit = False
    if pos < len(string) - length and string[pos + length] == "#":
        fit = False
    return fit

def get_possible_locations(group_len, string):
    """Een groep past ergens als:
    - op posities i tot i+n een ? of een # staat
    - op positie i + n + 1 en i - 1 een ? of een . staat. Dit geeft index errors bij te grote waarden en verkeerde uitkomsten bij negatieve index.
    """
    locations = []
    # loop de string af
    for i in range(0, len(string) - group_len + 1) :
        possible = True
        # op elke plek in de string, voor n vanaf string[i], kijk of er een . staat. Zo ja, dan is deze positie niet mogelijk.
        if not check_fit(group_len, string, i):
            possible = False
        if possible:
            locations.append(i)
    return locations

def check_combo(combo, lengths):
    possible = True
    # voor elke positie vanaf de tweede tot het eind geldt:
    # positie moet groter zijn dan de vorige + de lengte van de vorige + 1
    for i in range(1, len(combo)):
        if not (combo[i] > combo[i-1] + lengths[i-1]):
            possible = False
    return possible


def get_options(options, lengths):
    combos = list(itertools.product(*options))
    possible = []
    for c in combos:
        result = check_combo(c, lengths)
        if result:
            possible.append(c)
    return possible

def check_options(combos, lengths, string):
    # check of er geen hekjes staan op plaatsen die niet gecoverd worden door een groep, gegeven een bepaalde combo.
    options = []
    for combo in combos:
        # replace group locations with "X"
        string_new = string
        for i, pos in enumerate(combo):
            string_new = string_new[0:pos] + "X" * lengths[i] + string_new[pos + lengths[i]:]
        # check if any hashes are left in the string
        if not '#' in string_new:
            options.append(combo)
    return options


total = 0
for i, d in enumerate(data):
    string, group_sizes = d.split()
    group_sizes = list(map(int, group_sizes.split(",")))
    possible_locations = []
    # get possible locations for each group length
    for n in group_sizes:
        possible_locations.append(get_possible_locations(n, string))
    # check if locations would fit based on length
    options = get_options(possible_locations, group_sizes)
    # check if no hashes remain uncovered given this layout
    options = check_options(options, group_sizes, string)
    total += len(options)

print(total)
#assert total == 7173

aoc.end(start)
# 51 sec.