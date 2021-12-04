import AoC_tools.aoc_tools as aoc

data = aoc.string2list(path="C:/Users/Admin/SURFdrive/Code/advent_of_code/2021/4/input.txt", sep="\n\n")
aoc.lprint(data)
print(len(data))

boards = []
firstline = data[0]
numbers = firstline.split(",")
data = data[1:]
tmp = [line.split("\n") for line in data]
for i in range(len(tmp)):
    b = [(line.split()) for line in tmp[i]]
    print(b)
    boards.append(b)
    #aoc.make_grid(b)

class Bingo():

    def __init__(self, boards, numbers):
        self.boards = boards
        self.last_winner = None
        self.numbers = numbers
        self.winning_boards = set()
        self.draw = None

    @staticmethod
    def mark_number(board, number):
       for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == number:
                    board[i][j] = 'X'
       return board

    @staticmethod
    def check_board(board):
        ncols = len(board[0])
        nrows = len(board)
        # check rows
        for i in range(ncols):
            if all(x == 'X' for x in board[i]):
                return True
        # check cols
        # begin bij eerste element van elke rij
        for i in range(ncols):
            elements = []
            for j in range(nrows):
                elements.append(board[j][i])
            if all(x == 'X' for x in elements):
                return True
        return False


    def check_boards(self):
        for i in range(len(self.boards)):
            result = self.check_board(self.boards[i])
            if result:
                if i not in self.winning_boards:
                    print("bingo on board", i, "!")
                    self.winning_boards.add(i)
                    self.last_winner = i



    def get_winning(self):
        for i in range(len(self.numbers)):
            self.draw = i
            print("Number drawn:", self.numbers[i])
            for j in range(len(self.boards)):
                self.mark_number(self.boards[j], self.numbers[i])
            self.check_boards()
            if len(self.winning_boards) == len(self.boards):
                break
        print("losing board:", self.last_winner)
        print("draw:", self.draw)
        print("last drawn number:", self.numbers[self.draw])

bingo = Bingo(boards, numbers)
bingo.get_winning()
print("losing board:", bingo.last_winner)

sum = 0
for line in bingo.boards[bingo.last_winner]:
    for element in line:
        if element != 'X':
            sum += int(element)

print("sum:", sum)

answer = sum * int(bingo.numbers[bingo.draw])
print("answer:", answer)


