import copy

with open('input.txt') as f:
    data = f.read().split("\n")

for i in range(len(data)):
    data[i] = data[i].split(" (contains ")
    data[i][0] = data[i][0].split(" ")
    data[i][1] = data[i][1].replace(")", "")
    data[i][1] = data[i][1].split(", ")


def check_presence_in_foods(ingredient, allergen, foods):
    # if ingredient is not in all foods the allergen is in, it cannot be that allergen
    for food in foods:
        if allergen in food[1]:
            if ingredient not in food[0]:
                return False
    # als er nergens een false uitkomt, is het dus een allergen
    return True

ingredients = set()
allergens = set()

for d in data:
    ingredients.update(d[0])
    allergens.update(d[1])

unsafe_ingredients = set()

for i in ingredients:
    # if ingredient is not in all foods the allergen is in, it cannot be that allergen. If it cannot be any of the
    # allergens it's a safe food.
    for a in allergens:
        result = check_presence_in_foods(i, a, data)
        # als er ergens een true uitkomt bevat het ingredient een allergen en is het dus niet safe.
        if result:
            unsafe_ingredients.add(i)
            break

safe_ingredients = [i for i in ingredients if i not in unsafe_ingredients]
foods = copy.deepcopy(data)

def remove_ingredient(ingredient, foods):
    for food in foods:
        if ingredient in food[0]:
            food[0].remove(ingredient)

# remove safe ingredients from foods list
for i in safe_ingredients:
    remove_ingredient(i, foods)

matches = {}

def match_allergens(foods, allergen, matches):
    # check waar een allergen allemaal bij staat.
    suspect_ingredients = set()
    foods_with_allergen = []
    for food in foods:
        if allergen in food[1]:
            suspect_ingredients.update(food[0])
            foods_with_allergen.append(food[0])
    still_suspect = suspect_ingredients.copy()
    for i in suspect_ingredients:
        count = 0
        for f in foods_with_allergen:
            if i in f:
                count += 1
        if count < len(foods_with_allergen):
            still_suspect.remove(i)
    if len(still_suspect) == 1:
        matches[allergen] = list(still_suspect)[0]
        # remove the matched allergen and ingredient from the lists
        allergens.remove(allergen)
        to_remove = list(still_suspect)[0]
        remove_ingredient(to_remove, foods)

while len(allergens) > 0:
    allergens_left = allergens.copy()
    for a in allergens_left:
        match_allergens(foods, a, matches)

result = []
for i in sorted(matches):
    result.append(matches[i])

result = (",".join(result))

assert result == "kqv,jxx,zzt,dklgl,pmvfzk,tsnkknk,qdlpbt,tlgrhdh"