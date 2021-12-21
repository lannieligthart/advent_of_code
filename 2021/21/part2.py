
rolls = []
for i in [1, 2, 3]:
    for j in [1, 2, 3]:
        for k in [1, 2, 3]:
            rolls.append((i,j,k))

states = {}

class Game(object):

    def __init__(self, space1, score1, space2, score2):
        self.space1 = space1
        self.score1 = score1
        self.space2 = space2
        self.score2 = score2

    def __str__(self):
        return (f"Player 1 score: {self.score1}\nPlayer 2 score: {self.score2}")

    def play1(self, roll):
        # 1 beurt bestaat uit:
        # 1 roll
        # space updaten
        # score updaten op basis van space
        self.space1 += sum(roll)
        if self.space1 > 10:
            if self.space1 % 10 == 0:
                self.space1 = 10
            else:
                self.space1 = self.space1 % 10
        self.score1 += self.space1

    def play2(self, roll):
        self.space2 += sum(roll)
        if self.space2 > 10:
            if self.space2 % 10 == 0:
                self.space2 = 10
            else:
                self.space2 = self.space2 % 10
        self.score2 += self.space2


states = {
    (4, 0, 8, 0): 1
}

p1_wins = 0
p2_wins = 0

while len(states) > 0:
    newstates = {}
    for r1 in rolls:
        for r2 in rolls:
            for state, n in states.items():
                game = Game(*state)
                game.play1(roll=r1)
                game.play2(roll=r2)
                newstate = (game.space1, game.score1, game.space2, game.score2)
                if newstate in newstates:
                    newstates[newstate] += n
                elif newstate not in newstates:
                    newstates[newstate] = n
    states = newstates.copy()
    print(sum(states.values()))
    for key, value in newstates.items():
        if key[1] >= 21:
            p1_wins += value
            states.pop(key)
        elif key[3] >= 21:
            p2_wins += value
            states.pop(key)

    #print(states)

    print("P1 wins:", p1_wins)
    print("P2 wins:", p2_wins)
    print(sum(states.values()))