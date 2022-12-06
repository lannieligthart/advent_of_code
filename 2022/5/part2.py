from AoC_tools import aoc_tools as aoc
from collections import deque

def add_whitespace(str, maxlen):
    l = len(str)
    str += " " * (maxlen - l)
    return str

def read_stacks(stacks, n):
    deques = [deque() for i in range(n)]
    stacks.reverse()
    for s in stacks:
        letters = s[1::4]
        row = list([*letters])
        # per rij, plak de n-de letter aan de bijbehorende deque
        for i in range(len(row)):
            if row[i] != ' ':
                deques[i].append(row[i])
    return deques

def extract_move(move):
    move = move.split(" ")
    n, f, t = (int(move[1]), int(move[3]), int(move[5]))
    return (n, f, t)

def move(n, fr, to, stacks):
    fr = fr - 1
    to = to - 1
    tmp = deque()
    for i in range(n):
        tmp.append(stacks[fr][-1])
        stacks[fr].pop()
    for i in range(n):
        stacks[to].append(tmp[-1])
        tmp.pop()
    return stacks

def run(n, data):
    stacks = data[0].split("\n")[0:-1]
    maxlen = max(list(map(len, stacks)))
    stacks = list(map(add_whitespace, stacks, [maxlen]*len(stacks)))
    stacks = read_stacks(stacks, n)
    moves = data[1].split("\n")
    moves = list(map(extract_move, moves))
    for m in moves:
        stacks = move(*m, stacks)
    result = "".join([s[-1] for s in stacks])
    return result

data = aoc.read_input("testinput.txt", "\n\n")
assert run(3, data) == "MCD"
data = aoc.read_input("input.txt", "\n\n")
assert run(9, data) == "FSZWBPTBG"

