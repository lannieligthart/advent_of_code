with open('input.txt') as f:
    data = f.read().split("\n\n")

print(data)

player1 = data[0].split('\n')[1:]
player2 = data[1].split('\n')[1:]
player1 = [int(i) for i in player1]
player2 = [int(i) for i in player2]

print(player1, player2)

def play(p1, p2):
    draw = [p1.pop(0), p2.pop(0)]
    if draw[0] > draw[1]:
        print("player1 won!")
        draw.sort(reverse=True)
        player1.extend(draw)
    else:
        print("player2 won!")
        draw.sort(reverse=True)
        player2.extend(draw)
    print(player1, player2)

while len(player1) > 0 and len(player2) > 0:
    play(player1, player2)

if len(player1) > 0:
    player1.reverse()
    winner = player1
else:
    player2.reverse()
    winner = player2

print(winner)

products = []
for i, card in enumerate(winner, start=1):
    products.append(i*card)
print(products)
print(sum(products))

assert sum(products) == 33694