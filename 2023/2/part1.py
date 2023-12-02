with open("input.txt") as file:
    data = file.read().split("\n")

data = [d.replace(",", "") for d in data]
data = [d.replace(";", "") for d in data]

limits = {"red": 12, "green": 13, "blue": 14}

impossible_ids = set()
all_ids = set()

for d in data:
    game = d.split(": ")[0].split(" ")[1]
    outcomes = d.split(": ")[1].split(" ")
    all_ids.add(int(game))
    for i in range(0, len(outcomes)-1, 2):
        color = outcomes[i + 1]
        n = int(outcomes[i])
        if limits[color] < n:
            impossible_ids.add(int(game))
            break

result = sum(all_ids - impossible_ids)

assert result == 2176
