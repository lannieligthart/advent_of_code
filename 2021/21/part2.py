
rolls = []
for i in [1, 2, 3]:
    for j in [1, 2, 3]:
        for k in [1, 2, 3]:
            rolls.append((i,j,k))

states = {}

modulo10 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]

class Game(object):

    def __init__(self, space1, score1, space2, score2):
        self.space1 = space1
        self.score1 = score1
        self.space2 = space2
        self.score2 = score2

    def __str__(self):
        return (f"Player 1 score: {self.score1}\nPlayer 2 score: {self.score2}")

    def play(self, roll1, roll2):
        space1 = modulo10[self.space1 + sum(roll1)]
        score1 = self.score1 + space1
        space2 = modulo10[self.space2 + sum(roll2)]
        score2 = self.score2 + space2
        return Game(space1, score1, space2, score2)

    def play1(self, roll):
        # 1 beurt bestaat uit:
        # 1 roll
        # space updaten
        # score updaten op basis van space
        self.space1 = modulo10[self.space1 + sum(roll)]
        self.score1 += self.space1

    def play2(self, roll):
        self.space2 = modulo10[self.space2 + sum(roll)]
        self.score2 += self.space2

states = {
    (10, 0, 6, 0): 1
}

p1_wins = 0
p2_wins = 0

while len(states) > 0:
    newstates = {}
    for r1 in rolls:
        for r2 in rolls:
            for state, n in states.items():
                game = Game(*state).play(roll1=r1, roll2=r2)
                newstate = (game.space1, game.score1, game.space2, game.score2)
                if newstate[1] >= 21:
                    p1_wins += n
                elif newstate[3] >= 21:
                    p2_wins += n
                elif newstate in newstates:
                    newstates[newstate] += n
                elif newstate not in newstates:
                    newstates[newstate] = n
    states = newstates.copy()

    print("P1 wins:", int(p1_wins/27))
    print("P2 wins:", p2_wins)
    print(sum(states.values()))


#306719685234774