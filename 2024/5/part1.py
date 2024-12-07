import math

infile = "testinput.txt"
infile = "input.txt"

with open(infile) as f:
    data = f.read().split("\n\n")

rules = data[0].split("\n")
rules = [list(map(int, r.split("|"))) for r in rules]
existing_pages = []
list(map(existing_pages.extend, rules))
existing_pages = list(set(existing_pages))

updates = data[1].split("\n")
updates = [list(map(int, u.split(","))) for u in updates]

total = 0

def check_order(page1, page2, rules):
    for r in rules:
        if r[0] == page1 and r[1] == page2:
            return True
    return False

for update in updates:
    # remove missing pages
    update = [page for page in update if page in existing_pages]
    # check page order for each subsequent pair
    order_correct = True
    for i in range(len(update)-1):
        if not check_order(update[i], update[i+1], rules):
            order_correct = False
    if order_correct:
        total += update[math.floor(len(update)/2)]

print(total)

if infile == "testinput.txt":
    assert total == 143
elif infile == "input.txt":
    assert total == 6612
