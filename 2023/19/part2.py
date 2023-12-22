from AoC_tools import aoc22 as aoc
import re
from operator import mul
from functools import reduce

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


def process_rule(part, rule):
    # this is where we just go to accept or reject or the next workflow
    if len(rule.split(":")) == 1:
        return (part, rule)
    # this is a condition
    if len(rule.split(":")) == 2:
        rule = re.findall('([xmas])([><])([0-9]+):([a-zA-Z]+)', rule)[0]
        property = rule[0]
        operator = rule[1]
        cutoff = int(rule[2])
        outcome = rule[3]
        # if the cutoff falls within the current range, cut the range into two. Otherwise, don't split.
        oldrange = part[property]
        if cutoff > oldrange[0] and cutoff < oldrange[1]:
            if operator == "<":
                range1 = (oldrange[0], cutoff - 1)
                range2 = (cutoff, oldrange[1])
                # create new parts based on the split ranges
                part1 = part.copy()
                part1[property] = range1
                part2 = part.copy()
                part2[property] = range2
                # if <, the first range gets outcome (accept, reject or workflow), and first range gets next rule
                return (part1, outcome, part2, None)
            elif operator == ">":
                range1 = (oldrange[0], cutoff)
                range2 = (cutoff + 1, oldrange[1])
                # create new parts based on the split ranges
                part1 = part.copy()
                part1[property] = range1
                part2 = part.copy()
                part2[property] = range2
                return (part2, outcome, part1, None)
        else:
            if operator == "<":
                return (part, outcome)
            elif operator == ">":
                return (part, outcome)

results = dict()

def process_wf(part, wf):
    # start off with the first rule on the list
    rule = wf.pop(0)
    # if rule is only a workflow, process this workflow
    result = process_rule(part, rule)
    # unpack results
    if len(result) == 2:
        part1, part1_outcome = result
    elif len(result) == 4:
        part1, part1_outcome, part2, part2_outcome = result

    # outcome can be A/R/new wf/None. None means the next rule should be applied.
    if part1_outcome is None:
        # process the remainder of the workflow for this part
        process_wf(part1, wf)
    # If outcome is accept, add the processed result to the results dictionary
    elif part1_outcome == "A":
        print(f"result for {part1}: {part1_outcome}")
        ranges = list(part1.values())
        numbers = [r[1]+1 - r[0] for r in ranges]
        total = reduce(mul, numbers, 1)
        results[str(part1)] = total
    # if outcome is reject, we don't need to do anything else.
    elif part1_outcome == "R":
        print(f"result for {part1}: {part1_outcome}")
    # if outcome is a new workflow, process that new workflow.
    elif part1_outcome in workflows.keys():
        process_wf(part1, workflows[part1_outcome])
    # If there was also a second part that needs to be processed, do that here.
    # Second parts are the ones not processed by the rule but forwarded to the next, so only that needs to be done here.
    if len(result) == 4:
        if part2_outcome is None:
            process_wf(part2, wf)


# instead of the specified parts, we now start with one master part with all the ranges
partslist = [{"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}]

for part in partslist:
    process_wf(part, workflows["in"])

aoc.dprint(results)
total = 0
for value in results.values():
    total += value

print(total)
assert total == 132186256794011

