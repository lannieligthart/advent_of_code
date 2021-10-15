from math import ceil


def get_formulas(data):
    data = [d.split(" => ") for d in data]
    formulas = {}
    for d in data:
        if "," in d[0]:
            split_value = d[0].split(", ")
            formulas[d[1]] = split_value
        else:
            formulas[d[1]] = [d[0]]
    return formulas


class Chemical():

    def __init__(self, n, type):
        self.type = type
        self.n = n

    def __str__(self):
        return (str(self.n) + " " + self.type)

    @staticmethod
    def parse(string):
        n, type = string.split(" ")
        n = int(n)
        return Chemical(n, type)

    def multiply(self, factor):
        multiplied = self.n * factor
        result = Chemical(multiplied, self.type)
        return result


def get_base_elements(formulas):
    base_elements = []

    for key, value in formulas.items():
        if "ORE" in value[0]:
            element = key.split(" ")[1]
            base_elements.append(element)
    return base_elements


with open('testinput.txt') as f:
    data = f.read().split("\n")

formulas = get_formulas(data)

print("formulas:")
for key, value in formulas.items():
    print(key, value)
print("\n")

# bepaal wat de basiselementen zijn (A en B)
base_elements = get_base_elements(formulas)
base_formulas = {}

# bepaal de formules voor de basiselementen
for be in base_elements:
    for key, value in formulas.items():
        if be == key.split(" ")[1]:
            base_formulas[key] = value[0]

# print(base_formulas)

print("base elements are:")
print(base_elements, "\n")

leftover = {}


# bepaal hoeveel je van elk basiselement nodig hebt
def get_cost(element, amount):
    # lookup of cost in formula dictionary
    # multiply by factor specified
    for key, value in formulas.items():
        if element in key:
            # convert strings to chemicals
            value = [Chemical.parse(v) for v in value]### klopt dit wel??
            # units of production
            n_returned = int(key.split(" ")[0])
            # multiply each chemical by factor, if factor > unit of production
            if amount > n_returned:
                factor = ceil(amount / n_returned)
            else:
                factor = 1

            cost = []
            for chem in value:
                # amount after multiplication
                multiplied = chem.multiply(factor)
                cost.append(multiplied)
                product = factor * n_returned
                remainder = Chemical(type=element, n=product - amount)
                if remainder.type in leftover:
                    leftover[remainder.type] += remainder.n
                else:
                    leftover[remainder.type] = remainder.n
            # voor elk element in cost, ga na of er nog iets in leftover zit. Zo ja, trek dat van cost af en haal het
            # uit leftover.
            for chem in cost:
                if chem.type in leftover and leftover[chem.type] > 0:
                    # als er genoeg is, zet element op nul en trek af van leftover N.
                    if leftover[chem.type] >= chem.n:
                        leftover[chem.type] -= chem.n
                        chem.n = 0
                    # als er niet genoeg is, trek aanwezige aantal af van chem.n en zet leftover op nul.
                    elif leftover[chem.type] < chem.n:
                        chem.n -= leftover[chem.type]
                        leftover[chem.type] = 0
            print("\nReserve:")
            for key, value in leftover.items():
                print(key, value)
            return cost


# keep tabs of required base elements
required = {}  # nodig
for e in base_elements:
    required[e] = 0

cost = [Chemical.parse("1 FUEL")]
stop = False

while True:
    # Check of alle elementen in cost een basiselement zijn. Zo niet, dan moet de loop door blijven lopen.
    n_base = 0
    for chem in cost:
        if chem.type in base_elements:
            n_base += 1
    if n_base == len(cost):
        stop = True  # indien True, dan stopt de loop aan het eind.

    # show current cost
    print(" ".join([str(c) for c in cost]))
    # convert non-base elements by looking up their value and multiplying by the amount needed.
    # if any product is left-over, keep track of it
    tmp = []
    for chem in cost:
        # indien al een base element, dan hoeft er niks te veranderen. Zet bestaande element terug.
        if chem.type in base_elements:
            tmp.extend([chem])
        # indien geen base element, converteer en voeg toe aan tmp.
        elif chem.type not in base_elements:
            tmp.extend(get_cost(chem.type,
                                chem.n))  # let op: als de basisproductie meer is dan hier nodig, moet het restant ergens worden opgeslagen.
    cost = tmp.copy()

    if stop:
        break

final_cost = []

for c in cost:
    required[c.type] += c.n
for key, value in required.items():
    final_cost.append(Chemical(value, key))

amount_needed = []
for chem in final_cost:
    amount_needed.extend(get_cost(chem.type, chem.n))
pass

n_ore = 0
for chem in amount_needed:
    n_ore += chem.n

print(n_ore)

# bepaal hoeveel ORE je nodig hebt om minimaal die hoeveelheid te maken van elk basiselement
# 10/2 = 5 * 9 = 45 ORE voor 10 A
# 23/3 = 8 * 8 = 64 ORE voor 23 B
# 37/5 = 8 * 7 = 56 ORE voor 37 C
#
# amount_needed = 0
#
# for e in base_elements:
#     # get required
#     req = required[e]
#     # get per how many they are produced and how much ORE they cost
#     for key, value in base_formulas.items():
#         if e == key.split(" ")[1]:
#             per_n = int(key.split(" ")[0])
#             amount = int(value.split(" ")[0])
#             # divide required by unit of production and round
#             req_rounded = ceil(req/per_n)
#             amount_needed += req_rounded * amount
# print(amount_needed)
#
#
# # tel deze bedragen op.


