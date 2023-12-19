from AoC_tools import aoc22 as aoc
import re

with open("input.txt") as file:
    wf, parts = file.read().split("\n\n")

parts = parts.split("\n")
parts = [re.sub(r"[}{=xmas]", "", p) for p in parts]
parts = [p.split(",") for p in parts]

partslist = []
for p in parts:
    p = list(map(int, p))
    part = dict()
    part["x"], part["m"], part["a"], part["s"] = p
    partslist.append(part)

parts = partslist

workflows = dict()
wf = wf.split("\n")
wf = [w.replace("}", "").split("{") for w in wf]
workflows = {w[0]: w[1].split(",") for w in wf}


def process_rule(rule, part):
    if len(rule.split(":")) == 1:
            return rule
    if len(rule.split(":")) == 2:
        rule = re.findall('([xmas])([><])([0-9]+):([a-zA-Z]+)', rule)[0]
        if rule[1] == ">":
            if part[rule[0]] > int(rule[2]):
                return rule[3]
        elif rule[1] == "<":
            if part[rule[0]] < int(rule[2]):
                return rule[3]


def process_wf(wf, part):
    for rule in wf:
        result = process_rule(rule, part)
        if result == "A":
            return "accept"
        elif result == "R":
            return "reject"
        if result is None:
            pass
        else:
            return result


def process_part(part, workflows):
    score = 0
    next = "in"
    while True:
        if next == "accept":
            score += part["x"]
            score += part["m"]
            score += part["a"]
            score += part["s"]
            return score
        elif next == "reject":
            return 0
        else:
            next = process_wf(workflows[next], part)

total = 0
for part in partslist:
    total += process_part(part, workflows)

print(total)

assert total == 495298