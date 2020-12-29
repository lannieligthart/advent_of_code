with open('input.txt') as f:
    data = f.read().split("\n")

for i in range(len(data)):
    data[i] = data[i].split(" (contains ")
    data[i][0] = data[i][0].split(" ")
    data[i][1] = data[i][1].replace(")", "")
    data[i][1] = data[i][1].split(", ")



# def check_frequency(ingredient, allergen, foods):
#     # if ingredient is less frequent than allergen, it cannot be that allergen
#     # loop through all foods
#     # count presence of ingredient and allergen
#     i_count = 0
#     a_count = 0
#     for food in foods:
#         if ingredient in food:
#             i_count += 1
#         if allergen in food:
#             a_count += 1
#     # compare
#     if i_count < a_count:
#         return False
#     else:
#         return True



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

print(ingredients, allergens)

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

print(unsafe_ingredients)

safe_ingredients = [i for i in ingredients if i not in unsafe_ingredients]
print(safe_ingredients)

count = 0
for i in safe_ingredients:
    for food in data:
       if i in food[0]:
           count += 1

print(count)

assert count == 2493