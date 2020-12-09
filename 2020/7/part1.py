with open('input.txt') as f:
    data = f.read().split("\n")


class bag(object):

    def __init__(self, colour, content):
        self.colour = colour
        self.content = content

    def __str__(self):
        return("Colour: " + self.colour + "\nContent: " + str(self.content))


for i in range(len(data)):
    data[i] = data[i].replace(" bags", "")
    data[i] = data[i].replace(" bag", "")
    data[i] = data[i].replace(".", "")
    data[i] = data[i].replace(" no other", " 0")
    data[i] = data[i].split(" contain ")
    data[i][1] = data[i][1].split(", ")

#print(data)

all_bags = []

for d in data:
    colour = d[0]
    # content should be dictionary with colours as keys and counts as values
    content = {}
    content_tmp = d[1]
    for c in content_tmp:
        spl = c.split(" ", maxsplit=1)
        if int(spl[0]) > 0:
            content[spl[1]] = int(spl[0])
        elif spl[0] == 0:
            pass
    b = bag(colour=colour, content=content)
    all_bags.append(b)

# get all bags which hold a shiny gold bag
# then get all bag colours that hold these bags and add to collection
# and so on until content == 0

final_collection = set()
# current set
selection = set()
# set obtained in the last round, to be transported as input to next round
new_selection = set()

# starting point
selection.add('shiny gold')

while True:
    for b in all_bags:
        for colour in selection:
            if colour in b.content:
                # add new bag colour
                new_selection.add(b.colour)
    # add start colours to the final collection
    for c in selection:
        final_collection.add(c)
    if len(new_selection) == 0:
        break
    # replace old selection by the new one
    selection = new_selection
    new_selection = set()

# shiny gold zelf telt niet mee
final_collection.remove('shiny gold')

print(final_collection)
print(len(final_collection))
assert len(final_collection) == 378

