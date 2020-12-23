input = "193467258"

class CircleGame(object):

    def __init__(self, input):
        self.cups = [int(input[i]) for i, cup in enumerate(input)]
        self.destination_number = None
        self.current = 0
        self.lowest = min(x for x in self.cups if x is not None)
        self.highest = max(x for x in self.cups if x is not None)

    def __str__(self):
        txt = """
cups: {0}
current cup: {1}
""".format(self.cups, self.cups[self.current])
        return txt

    @property
    def destination_index(self):
        return self.cups.index(self.destination_number)

    def move(self):
        print(self.cups)
        print("current:", self.cups[self.current])
        # remove the first 3 cups after current cup
        removed = []
        for i in range(self.current + 1, self.current + 4):
            removed.append(self.cups[i % len(self.cups)])
            self.cups[i % len(self.cups)] = None

        self.destination_number = self.cups[self.current] - 1
        # index van de cup met dat nummer
        while True:

            if self.destination_number in self.cups:
                #self.destination_index = self.cups.index(self.destination_number)
                break
            elif self.destination_number < self.lowest:
                self.destination_number = self.highest
                #self.destination_index = self.cups.index(self.destination_number)
                if self.destination_number in self.cups:
                    #self.destination_index = self.cups.index(self.destination_number)
                    break
            self.destination_number -= 1
        print("pick up:", removed)
        #print("destination index:", self.destination_index)
        print("destination:", self.cups[self.destination_index], "\n")
        # move everything from self.current + 4 thru self.destination 3 places back
        start = (self.current + 4) % len(self.cups)
        stop = (self.destination_index + 1) % len(self.cups)
        if stop >= start:
            to_move = self.cups[start:stop]
        elif stop < start:
            to_move = self.cups[start:]
            for i in range(start, len(self.cups)):
                self.cups[i % len(self.cups)] = None
            for i in range(stop):
                to_move.append(self.cups[i % len(self.cups)])
                self.cups[i % len(self.cups)] = None
        for i in range(start, stop):
            self.cups[i % len(self.cups)] = None
        # insert 3 places back
        start -= 3
        for i in range(len(to_move)):
            self.cups[(i + start) % len(self.cups)] = to_move[i]
            last_pos = i + start
        # de laatste positie waar iets wordt geinsert is de destination cup
        start = last_pos + 1
        for i in range(len(removed)):
            self.cups[(start + i) % len(self.cups)] = removed[i]
        self.current += 1
        self.current = self.current % len(self.cups)

game = CircleGame(input)
#print(game)

for _ in range(101):
    game.move()



# 3 na current are emptied
# current + 4 tot en met destination shift 3 to the left
# na destination komen de verwijderde waarden
# de rest blijft hetzelfde

25468379