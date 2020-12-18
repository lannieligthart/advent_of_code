def eliminate_brackets(data):
    # result equals data unless it's modified by the code below.
    result = data
    for i in range(len(data)):
        if data[i] == "(":
            start = i
        elif data[i] == ")":
            stop = i+1
            if start is not None:
                e = eval_different_order(data[start+1:stop-1])
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
        #print(after)
    return after

def eval_different_order(data):
    data = eliminate_all_brackets(data)
    # if there are no multiplications, no further modifications are needed
    if not "+" in data:
        return eval(data)
    # otherwise, evaluate + first
    i = 0
    data = data.split(" ")
    # voeg eerste positie in
    result = [data[0]]
    while "+" in data and (i + 2) < len(data):
        # if the operator in this sequence is a plus, evaluate and add to result. Otherwise, skip two positions.
        if data[i+1] == "+":
            expr = result[-1] + data[i+1] + data[i+2]
            result = result[0:-1]
            result.append(str(eval(expr)))
            #print(result)
        else:
            # voeg laatste twee items toe
            result.extend(data[i+1:i+3])
        i += 2
    return eval(" ".join(result))


data = "1 + (2 * 3) + (4 * (5 + 6))"
assert eval_different_order(data) == 51
data = "2 * 3 + (4 * 5)"
assert eval_different_order(data) == 46
data = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
assert eval_different_order(data) == 1445
data = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
assert eval_different_order(data) == 669060
data = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
assert eval_different_order(data) == 23340

with open('input.txt') as f:
    data = f.read().split("\n")

results = []
for d in data:
    results.append(eval_different_order(d))

print(sum(results))
assert sum(results) == 231235959382961





