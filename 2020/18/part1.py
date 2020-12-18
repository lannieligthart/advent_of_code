def eliminate_brackets(data):
    # result equals data unless it's modified by the code below.
    result = data
    for i in range(len(data)):
        if data[i] == "(":
            start = i
        elif data[i] == ")":
            stop = i+1
            if start is not None:
                e = eval_in_order(data[start+1:stop-1])
                result = data[0:start] + str(e) + data[stop:]
                start = None
                stop = None
    return result

def eliminate_all_brackets(data):
    before = data
    while True:
        after = eliminate_brackets(before)
        if after == before:
            break
        before = after
    return after

def eval_in_order(data):
    data = eliminate_all_brackets(data)
    i = 0
    data = data.split(" ")
    result = data[0]
    while (i + 2) < len(data):
        expr = result + data[i+1] + data[i+2]
        # make this a string again so it can be combined with the rest of the input string and evaluated
        result = str(eval(expr))
        i += 2
    return int(result)

data = "2 * 3 + (4 * 5)"
assert eval_in_order(data) == 26
data = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
assert eval_in_order(data) == 437
data = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
assert eval_in_order(data) == 12240
data = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
assert eval_in_order(data) == 13632

with open('input.txt') as f:
    data = f.read().split("\n")

results = []
for d in data:
    results.append(eval_in_order(d))

print(sum(results))
assert sum(results) == 8929569623593




