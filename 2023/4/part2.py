import re
with open("input.txt") as file:
    data = file.read().split("\n")

class Card(object):

    def __init__(self, id, winning, numbers):
        self.id = id
        self.points = len(winning.intersection(numbers))
        self.count = 1
        self.additions = list(range(self.id + 1, self.id + self.points + 1))

cards = dict()

data = [re.sub(r'Card\s+', '', line) for line in data]
data = [re.split(r'[:|]', line) for line in data]

for line in data:
    id, winning, numbers = line
    winning = set(map(int, winning.split()))
    numbers = set(map(int, numbers.split()))
    c = Card(int(id), winning, numbers)
    cards[c.id] = c

for id in list(cards.keys()):
    for a in cards[id].additions:
        cards[a].count += cards[id].count

total = 0
for c in cards.values():
    total += c.count

assert total == 8736438
