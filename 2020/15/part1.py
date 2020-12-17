

class NumberGame(object):

    def __init__(self, numbers):
        self.numbers = numbers
        self.numbers_spoken = list()
        self.times_spoken = dict()
        self.last_time_spoken = dict()
        self.second_last_time_spoken = dict()
        self.turns_completed = 0

    def __str__(self):
        return """
        Numbers spoken: {0}
        Times spoken: {1}
        Last time spoken: {2}
        Turns completed: {3}""".format(str(self.numbers_spoken), str(self.times_spoken), str(self.last_time_spoken),
                                       str(self.turns_completed))

    def first_turn(self):
        for i in range(len(self.numbers)):
            self.turns_completed += 1
            self.numbers_spoken.append(self.numbers[i])
            self.times_spoken[self.numbers[i]] = 1
            self.last_time_spoken[self.numbers[i]] = self.turns_completed
        print(self)

    def turn(self):
        number = self.numbers_spoken[-1]
        self.turns_completed += 1
        # speak new number
        if self.times_spoken[number] == 1:
            self.numbers_spoken.append(0)
        elif self.times_spoken[number] > 1:
            self.numbers_spoken.append(self.last_time_spoken[number] - self.second_last_time_spoken[number])
        # update last spoken number
        number = self.numbers_spoken[-1]
        # if this new number has been spoken before:
        try:
            self.times_spoken[number] += 1
            self.second_last_time_spoken[number] = self.last_time_spoken[number]
        # if not, set times spoken and last time spoken for the first time.
        except KeyError:
            self.times_spoken[number] = 1
        self.last_time_spoken[number] = self.turns_completed
        #print(self)

testdata = [0,3,6]

def run_game(data):
    game = NumberGame(data)
    game.first_turn()
    while game.turns_completed < 2020:
        game.turn()
    print(game.numbers_spoken[-1])
    return game.numbers_spoken[-1]

assert run_game(testdata) == 436

data = [8,0,17,4,1,12]

run_game(data)

assert run_game(data) == 981