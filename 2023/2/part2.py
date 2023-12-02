with open("input.txt") as file:
    data = file.read().split("\n")

data = [d.replace(",", "") for d in data]
data = [d.replace(";", "") for d in data]

powers = []

for d in data:
    game = d.split(": ")[0].split(" ")[1]
    outcomes = d.split(": ")[1].split(" ")
    limits = {"red": 0, "green": 0, "blue": 0}
    for i in range(0, len(outcomes)-1, 2):
        color = outcomes[i + 1]
        n = int(outcomes[i])
        if limits[color] < n:
            limits[color] = n
    powers.append(limits["red"] * limits["green"] * limits["blue"])

result = sum(powers)

assert result == 63700