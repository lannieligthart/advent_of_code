with open("input.txt") as file:
    data = file.read().split("\n")

data = [d.split(": ")[1] for d in data]
data = [d.split(" | ") for d in data]

def process_card(card):
    winning = set(card[0].split())
    my_numbers = set(card[1].split())
    score = 0
    points = len(my_numbers.intersection(winning))
    if points > 0:
        score = 2 ** (points - 1)
    return score

total = 0
for card in data:
    total += process_card(card)

assert total == 24542

