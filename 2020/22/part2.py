with open('input.txt') as f:
    data = f.read().split("\n\n")

p1 = data[0].split('\n')[1:]
p2 = data[1].split('\n')[1:]
p1 = [int(i) for i in p1]
p2 = [int(i) for i in p2]

class Game(object):

    def __init__(self, p1, p2):
        self.p1_deck = p1
        self.p2_deck = p2
        self.p1_decks = []
        self.p2_decks = []
        self.subgame = None
        self.winner = None
        self.round = 0

    def play_round(self):
        self.round += 1
        self.draw = [self.p1_deck.pop(0), self.p2_deck.pop(0)]
        #print("player 1 plays", self.draw[0])
        #print("player 2 plays", self.draw[1])
        """if both players have at least as many cards in their own decks as the number on the card they just dealt, the 
        winner of the round is determined by recursing into a sub-game of Recursive Combat."""
        if len(self.p1_deck) >= self.draw[0] and len(self.p2_deck) >= self.draw[1]:
            #print("start sub-game")
            p1_new_deck = self.p1_deck[0:self.draw[0]]
            p2_new_deck = self.p2_deck[0:self.draw[1]]
            self.subgame = Game(p1_new_deck, p2_new_deck)
            self.subgame.play()
            # winner gets the last draw of the current game
            if self.subgame.winner == self.subgame.p1_deck:
                self.p1_deck.extend([self.draw[0], self.draw[1]])
            elif self.subgame.winner == self.subgame.p2_deck:
                self.p2_deck.extend([self.draw[1], self.draw[0]])
        elif self.draw[0] > self.draw[1]:
            #print("player1 won round", self.round)
            self.p1_deck.extend([self.draw[0], self.draw[1]])
        else:
            #print("player2 won round", self.round)
            self.p2_deck.extend([self.draw[1], self.draw[0]])
        #print(self.p1_deck, self.p2_deck)

    def play(self):
        while len(self.p1_deck) > 0 and len(self.p2_deck) > 0:
            """if there was a previous round in this game that had exactly the same cards in the same order in the same 
            players' decks, the game instantly ends in a win for player 1."""
            if self.p1_deck in self.p1_decks and self.p2_deck in self.p2_decks:
                #print("same deck as before, player 1 won!")
                break
            self.p1_decks.append(self.p1_deck[0:])
            self.p2_decks.append(self.p2_deck[0:])
            self.play_round()

        if len(self.p1_deck) > 0:
            #print("player 1 won round", self.round)
            #print("player 1 won the game!")
            self.winner = self.p1_deck
        else:
            #print("player 2 won round", self.round)
            #print("player 2 won the game!")
            self.winner = self.p2_deck

game = Game(p1, p2)
game.play()
print(game.winner)

# compute answer
winner = game.winner
winner.reverse()
products = []
for i, card in enumerate(winner, start=1, ):
    print(i, card)
    products.append(i*card)
print(products)
print(sum(products))

