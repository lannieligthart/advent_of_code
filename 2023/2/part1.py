with open("input.txt") as file:
    data = file.read().split("\n")

data = [d.replace(",", "") for d in data]
data = [d.replace(";", "") for d in data]
max_red = 12
max_green = 13
max_blue = 14

impossible_ids = set()
all_ids = set()

for d in data:
    game = d.split(": ")[0].split(" ")[1]
    outcomes = d.split(": ")[1].split(" ")
    all_ids.add(int(game))
    for i in range(0, len(outcomes)-1, 2):
        color = outcomes[i + 1]
        n = int(outcomes[i])
        if color == "green" and n > max_green:
            impossible_ids.add(int(game))
        elif color == "red" and n > max_red:
            impossible_ids.add(int(game))
        elif color == "blue" and n > max_blue:
            impossible_ids.add(int(game))

assert sum(all_ids - impossible_ids) == 2176
