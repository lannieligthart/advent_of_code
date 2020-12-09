with open('input.txt') as f:
    data = f.read().split("\n")


class bag(object):

    def __init__(self, colour, content):
        self.colour = colour
        self.content = content

    def __str__(self):
        return("Colour: " + self.colour + "\nContent: " + str(self.content))

    def n(self):
        return sum(self.content.values())


for i in range(len(data)):
    data[i] = data[i].replace(" bags", "")
    data[i] = data[i].replace(" bag", "")
    data[i] = data[i].replace(".", "")
    data[i] = data[i].replace(" no other", " 0")
    data[i] = data[i].split(" contain ")
    data[i][1] = data[i][1].split(", ")

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

# compute contents:
# get the contents of a bag
# colour * number, colour * number
# add up the total number in this bag, this is total number
# add the colours to selection and get their content number * the number in the previous bag
# for each of those, get the colours and accompanying numbers (i.e. the content)
# make this set the new input

# then get all bag colours that hold these bags and add to collection
# and so on until content == 0

selection = ['shiny gold']
new_selection = []
count = 0

while True:
    for colour in selection:
        for b in all_bags:
            if b.colour == colour:
                colours = list(b.content.keys())
                numbers = list(b.content.values())
                count += sum(numbers)
                for i in range(len(colours)):
                    new_selection.extend([colours[i]] * numbers[i])

    #print(new_selection)
    if len(new_selection) == 0:
        break
    selection = new_selection
    new_selection = []

print(count)

assert count == 27526