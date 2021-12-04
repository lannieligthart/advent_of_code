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


def mark_number(board, number):
   for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == number:
                board[i][j] = 'X'
   return board

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

def check_boards(boards):
    for i in range(len(boards)):
        result = check_board(boards[i])
        if result:
            print("bingo on board", i, "!")
            return int(i)



def get_winning(numbers, boards):
    for i in range(len(numbers)):
        print("Number drawn:", numbers[i])
        for j in range(len(boards)):
            mark_number(boards[j], numbers[i])
        result = check_boards(boards)
        if result is not None:
            print("Number announced was", numbers[i])
            print("round", i)
            print("winning board:", result, "(eigenlijk", result+1, ")")
            return (result, i)

winning_board, bingo_round = get_winning(numbers, boards)
print(bingo_round)
print(winning_board)

winner = boards[winning_board]

sum = 0
for line in winner:
    for element in line:
        if element != 'X':
            sum += int(element)

print("sum:", sum)

answer = sum * int(numbers[bingo_round])
print("answer:", answer)

assert answer == 71708
