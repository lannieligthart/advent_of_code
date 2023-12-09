with open("input.txt") as file:
    data = file.read().split("\n")


class Card(object):

    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid

    @property
    def type(self):
        counts = dict()
        for c in cards:
            counts[c] = self.hand.count(c)
        counts = list(counts.values())
        if 5 in counts:
            return "five_of_a_kind"
        elif 4 in counts:
            return "four_of_a_kind"
        elif 2 in counts and 3 in counts:
            return "full_house"
        elif 3 in counts:
            return "three_of_a_kind"
        elif counts.count(2) >= 2:
            return "two_pair"
        elif counts.count(2) == 1:
            return "one_pair"
        elif counts.count(1) == 5:
            return "high_card"


    @property
    def strength(self):
        strengths = {"five_of_a_kind": 6,
                     "four_of_a_kind": 5,
                     "full_house": 4,
                     "three_of_a_kind": 3,
                     "two_pair": 2,
                     "one_pair": 1,
                     "high_card": 0}
        return strengths[self.type]


cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

hands_dict = dict()

for d in data:
    hand, bid = d.split()
    hands_dict[hand] = Card(hand, bid)


def compare_hands(h1, h2):
    # compare by type.
    if h1.strength > h2.strength:
        return h1.hand
    elif h2.strength > h1.strength:
        return h2.hand
    # if that's a tie, compare by card value, starting with the first card.
    for i in range(5):
        if cards.index(h1.hand[i]) < cards.index(h2.hand[i]):
            return h1.hand
        elif cards.index(h2.hand[i]) < cards.index(h1.hand[i]):
            return h2.hand


hands = [d.split()[0] for d in data]
bids = [d.split()[1] for d in data]


def bubble_sort(hands):
    n = len(hands)
    swapped = False
    for i in range(n - 1):
        # Last i elements are already in place so we can skip them
        for j in range(0, n - i - 1):
            if compare_hands(hands_dict[hands[j]], hands_dict[hands[j+1]]) == hands[j]:
                swapped = True
                hands[j], hands[j + 1] = hands[j + 1], hands[j]
        if not swapped:
            return


bubble_sort(hands)
total = 0

for i, h in enumerate(hands):
    rank = i + 1
    bid = int(hands_dict[h].bid)
    total += bid * rank

assert total == 248113761

