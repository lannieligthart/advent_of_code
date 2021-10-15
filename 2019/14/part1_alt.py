


def getId(name):
    for i, ing in enumerate(inventory):
        if (ing[0] == name):
            return i
    return -1


def getRecipeId(name):
    for i, line in enumerate(lines):
        if (line[1][1] == name):
            return i
    return -1


lines = open("testinput.txt").readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip('\n').split(" => ")
    lines[i][0] = lines[i][0].split(", ")
    lines[i][1] = lines[i][1].split(" ")
    for j in range(len(lines[i][0])):
        lines[i][0][j] = lines[i][0][j].split(" ")

inventory = []

for line in lines:
    ingredients = line[0]
    for words in ingredients:
        name = words[1]

        if [name, 0] not in inventory:
            inventory.append([name, 0])
    name = line[1][1]
    if [name, 0] not in inventory:
        inventory.append([name, 0])

# print(inventory)
# print(getRecipeId("QCMJ"))
inventory[getId("FUEL")][1] = -1
finished = False

while (not finished):

    controlFinished = False

    for ingredient in inventory:
        if (ingredient[0] == "ORE"):
            continue
        # if we have a negative amount of any ingredient, we create it using the recipe
        elif (ingredient[1] < 0):
            recipeId = getRecipeId(ingredient[0])
            for recipeIngredient in lines[recipeId][0]:
                ingId = getId(recipeIngredient[1])
                inventory[ingId][1] -= int(recipeIngredient[0])
            ingId = getId(lines[recipeId][1][1])
            inventory[ingId][1] += int(lines[recipeId][1][0])
            controlFinished = True
    if (controlFinished == False):
        finished = True
print(inventory[getId("ORE")][1])

print(inventory)
