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
        else:
            pass
    return False

def check_update_order(update, rules):
    order_correct = True
    for i in range(len(update)-1):
        if not check_order(update[i], update[i+1], rules):
            order_correct = False
    return order_correct

def fix_order(update, rules):
    update = remove_duplicates(update)
    fixed_update = update.copy()
    while True:
        for i in range(len(update)-1):
            if not check_order(update[i], update[i + 1], rules):
                # swap the elements
                fixed_update[i] = update[i+1]
                fixed_update[i+1] = update[i]
            update = fixed_update.copy()
        if check_update_order(update, rules):
            return fixed_update

def remove_duplicates(update):
    return list(set([page for page in update]))

for update in updates:
    # remove missing pages
    update = [page for page in update if page in existing_pages]
    # check page order
    if not check_update_order(update, rules):
        fixed_update = fix_order(update, rules)
        total += fixed_update[math.floor(len(update)/2)]

print(total)

if infile == "testinput.txt":
    assert total == 123
elif infile == "input.txt":
    assert total == 4944
