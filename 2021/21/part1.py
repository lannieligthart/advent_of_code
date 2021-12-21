
class Die(object):

    def __init__(self, state=0):
        self.state = state

    def roll(self):
        self.state += 1
        if self.state == 101:
            self.state = 1
        return self.state

class Player(object):

    def __init__(self, name, space, score=0):
        self.space = space
        self.score = score
        self.name = name

    def move(self, steps):
        print("Rolled", steps)
        self.space += steps
        if self.space > 10:
            if self.space % 10 == 0:
                self.space = 10
            else:
                self.space = self.space % 10
        print("Moved to space:", self.space)

    def play(self, die, n):
        for i in range(n):
            steps = die.roll()
            self.move(steps)
        self.score += self.space
        print(self.name, "score:", self.score)


die = Die()

# example
p1 = Player("player 1", space=4)
p2 = Player("player 2", space=8)

# real data
p1 = Player("player 1", space=10)
p2 = Player("player 2", space=6)

i = 1
n_turns = 0
while True:
    print("Turn", i)
    p1.play(die, 3)
    n_turns += 3
    scores = [p1.score, p2.score]
    if p1.score >= 1000:
        break
    p2.play(die, 3)
    n_turns += 3
    scores = [p1.score, p2.score]
    if p2.score >= 1000:
        break
    i += 1

result = n_turns * min(scores)
assert result == 900099