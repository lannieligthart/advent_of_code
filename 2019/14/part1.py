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

    @property
    def cost(self):
        for key, value in formulas.items():
            if self.type in key:
                # convert strings to chemicals
                unit_cost = [Chemical.parse(v) for v in value]
                n_returned = int(key.split(" ")[0])
                # multiply each chemical by factor needed, if amount needed > unit of production (otherwise example 3 wont'work)
                if self.n > n_returned:
                    factor = ceil(self.n / n_returned)
                else:
                    factor = 1
                multiplied_cost = [c.multiply(factor) for c in unit_cost]
                # units of production
                return multiplied_cost

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

def deduplicate(cost):
    admin = {}
    for chem in cost:
        n, type = str(chem).split(" ")
        n = int(n)
        if type in admin:
            admin[type] += n
        else:
            admin[type] = n
    cost_updated = []
    for key, value in admin.items():
        cost_updated.append(Chemical(type=key, n=value))
    return cost_updated

with open('testinput.txt') as f:
    data = f.read().split("\n")

formulas = get_formulas(data)

print("formulas:")
for key, value in formulas.items():
    print(key, value)
print("\n")

# bepaal wat de basiselementen zijn (A en B)
base_elements = get_base_elements(formulas)

# startpunt
cost = [Chemical.parse("1 FUEL")]

stop = False
while True:
    # show current cost
    cost = deduplicate(cost) # deze stap is nodig voor voorbeeld 4
    print(" ".join([str(c) for c in cost]))
    # Check of alle elementen in cost een basiselement zijn. Zo niet, dan moet de loop door blijven lopen.
    n_base = 0
    for chem in cost:
        if chem.type in base_elements:
            n_base += 1
    if n_base == len(cost):
        stop = True  # indien True, dan stopt de loop aan het eind.
    for i in range(len(cost)):
        # indien geen base element, vervang door de cost van dit element en breek uit de for loop, die daarna weer
        # bij het begin begint, waardoor elk element eerst helemaal wordt doorlopen tot het basiselement alvorens verder
        # te gaan naar het volgende. Ik weet niet of dit de goede strategie is. Break weghalen maakt in elk geval wel
        # voorbeeld 4 stuk.
        if cost[i].type not in base_elements:
            addition = cost[i].cost
            cost.pop(i)
            cost.extend(addition)
            break
    if stop:
        break

final_cost = []
required = {}
for e in base_elements:
    required[e] = 0
    
cost = deduplicate(cost)
for c in cost:
    required[c.type] += c.n
print("total required:")
for key, value in required.items():
    print(key, value)
for key, value in required.items():
    final_cost.append(Chemical(value, key))

amount_needed = []
for chem in final_cost:
    amount_needed.extend(chem.cost)
pass

n_ore = 0
for chem in amount_needed:
    n_ore += chem.n

print(n_ore)
