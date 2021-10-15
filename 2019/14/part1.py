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

def get_hierarchy(formulas):
    # dict to store elements and their level
    elements = {
        "ORE": 0
    }
    next_level = 1
    while True:
        n_elements = len(elements)
        # loop alle formules door
        for product, recipe in formulas.items():
            ingredients = []
            # voor elke formule, loop de ingredienten langs
            for ingredient in recipe:
                ingredients.append(ingredient.split(" ")[1])
                # als alle ingredienten in deze formule maximaal van het laatst bepaalde niveau zijn, dan is het product
                # een element van een niveau hoger. In dat geval moet het worden toegevoegd aan de dictionary.
            if all(i in elements and elements[i] < next_level for i in ingredients):
                new_element = product.split(" ")[1]
                if new_element not in elements:
                    elements[new_element] = next_level
        cur_level_chems = []
        for ingredient, level in elements.items():
            if level == next_level:
                cur_level_chems.append(ingredient)
        if "FUEL" in elements:
            return elements
        next_level += 1

leftover = {}

class Chemical():

    def __init__(self, n, type):
        self.type = type
        self.n = n

    def __str__(self):
        return(str(self.n) + " " + self.type)

    @property
    def cost(self):
        """based on self.n and self.type, calculates the cost of this element given the N required."""
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
                # handle leftovers
                remainder = factor*n_returned - self.n
                if self.type in leftover:
                    leftover[self.type] += remainder
                else:
                    leftover[self.type] = remainder
                print("Need", self.n, self.type)
                print(factor, "reactions produces", factor*n_returned)
                print("leftover:", factor*n_returned - self.n)
                ### check if any of the ingredients are still in stock. If so, these can be deduced from multiplied_costs.
                for c in multiplied_cost:
                    if c.type in leftover:
                        if c.n <= leftover[c.type]:
                            leftover[c.type] -= c.n
                            c.n = 0
                        elif c.n > leftover[c.type]:
                            c.n -= leftover[c.type]
                            leftover[c.type] = 0
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

levels = get_hierarchy(formulas)

# startpunt
cost = [Chemical.parse("1 FUEL")]

def sort_cost(cost, levels):
    # sorteer cost op basis van welk level elk element is (begin met elementen dichtst bij FUEL).
    # cost is een lijst van chemicals die we dus moeten sorteren.
    maxlevel = levels["FUEL"]
    i = maxlevel
    cost_sorted = []
    while i >= 0:
        for c in cost:
            if levels[c.type] == i:
                cost_sorted.append(c)
        i -= 1
    return cost_sorted

stop = False
while True:
    # show current cost
    cost = deduplicate(cost) # deze stap is nodig voor voorbeeld 4
    print(" ".join([str(c) for c in cost]))
    cost = sort_cost(cost, levels)


    # Check of alle elementen in cost een basiselement zijn. Zo niet, dan moet de loop door blijven lopen.
    n_base = 0
    for chem in cost:
        if chem.type in ["ORE"]:
            n_base += 1
    if n_base == len(cost):
        stop = True  # indien True, dan stopt de loop aan het eind.
    for i in range(len(cost)):
        # indien geen base element, vervang door de cost van dit element en breek uit de for loop, die daarna weer
        # bij het begin begint, waardoor elk element eerst helemaal wordt doorlopen tot het basiselement alvorens verder
        # te gaan naar het volgende. Ik weet niet of dit de goede strategie is. Break weghalen maakt in elk geval wel
        # voorbeeld 4 stuk.
        if cost[i].type not in ["ORE"]:
            addition = cost[i].cost
            cost.pop(i)
            cost.extend(addition) # deze volgorde maakt uit!
            break
    if stop:
        break

n_ore = cost[0].n
assert n_ore == 365768
