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
        return(str(self.n) + " " + self.type)

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

print(base_formulas)



print("base elements are:")
print(base_elements, "\n")

# bepaal hoeveel je van elk basiselement nodig hebt
def get_cost(element, factor):
    # lookup of cost in formula dictionary
    # multiply by factor specified
    for key, value in formulas.items():
        if element in key:
            value = [Chemical.parse(v) for v in value]
            value = [v.multiply(factor) for v in value]
            value = [str(v) for v in value]
            #print("the cost of ", factor, element, "is:")
            #print(value)
            return value


# keep tabs of required base elements
required = {}
for e in base_elements:
    required[e] = 0


cost = []
new_cost = ["1 FUEL"]
while True:
    # als alle elementen in cost een basiselement zijn runt de cyclus nog 1 keer en stopt dan.
    n_base = 0
    for chem in cost:
        if chem.type in base_elements:
            n_base += 1
    # update cost
    cost = [Chemical.parse(nc) for nc in new_cost]
    print(" ".join([str(c) for c in cost]))
    new_cost = []
    for chem in cost:
        if chem.type in base_elements:
            new_cost.extend([str(chem)])
        elif chem.type not in base_elements:
            new_cost.extend(get_cost(chem.type, chem.n))
    if n_base == len(cost):
        for c in cost:
            required[c.type] += c.n
        for key, value in required.items():
            print(key, value)
        break



# bepaal hoeveel ORE je nodig hebt om minimaal die hoeveelheid te maken van elk basiselement
# 10/2 = 5 * 9 = 45 ORE voor 10 A
# 23/3 = 8 * 8 = 64 ORE voor 23 B
# 37/5 = 8 * 7 = 56 ORE voor 37 C

amount_needed = 0

for e in base_elements:
    # get required
    req = required[e]
    # get per how many they are produced and how much ORE they cost
    for key, value in base_formulas.items():
        if e == key.split(" ")[1]:
            per_n = int(key.split(" ")[0])
            amount = int(value.split(" ")[0])
            # divide required by unit of production and round
            req_rounded = ceil(req/per_n)
            amount_needed += req_rounded * amount
            print(amount_needed)


# tel deze bedragen op.


