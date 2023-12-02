with open("input.txt") as file:
    data = file.read().split("\n")

data = [d.replace(",", "") for d in data]
data = [d.replace(";", "") for d in data]

powers = []

for d in data:
    game = d.split(": ")[0].split(" ")[1]
    outcomes = d.split(": ")[1].split(" ")
    all_ids.add(int(game))
    max_red = 0
    max_green = 0
    max_blue = 0
    for i in range(0, len(outcomes)-1, 2):

        color = outcomes[i + 1]
        n = int(outcomes[i])
        if color == "green" and n > max_green:
            max_green = n
        elif color == "red" and n > max_red:
            max_red = n
        elif color == "blue" and n > max_blue:
            max_blue = n
    powers.append(max_green * max_red * max_blue)

assert(sum(powers) == 63700)