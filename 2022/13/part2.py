import AoC_tools.aoc22 as aoc

def compare_ints(left, right):
    if left < right:
        return True
    elif right < left:
        return False

def compare_lists(left, right):
    if isinstance(left, str):
        left = eval(left)
    if isinstance(right, str):
        right = eval(right)
    try:
        for i in range(max([len(left), len(right)])):
            if isinstance(left[i], int) and isinstance(right[i], int):
                result = compare_ints(left[i], right[i])
            elif isinstance(left[i], list) and isinstance(right[i], list):
                result = compare_lists(left[i], right[i])
            elif isinstance(left[i], list) and isinstance(right[i], int):
                r_tmp = [right[i]]
                result = compare_lists(left[i], r_tmp)
            elif isinstance(left[i], int) and isinstance(right[i], list):
                l_tmp = [left[i]]
                result = compare_lists(l_tmp, right[i])
            if result:
                return True
            elif result is False:
                return False
    except IndexError:
        if len(left) < len(right):
            return True
        elif len(left) > len(right):
            return False

data = aoc.read_input("input.txt", "\n")
data = [eval(d) for d in data if d != '']

def sort_packages(data):
    # add the two divider packets
    data.extend([[[2]], [[6]]])
    # perform insertion sort
    ordered = [data[-1]]
    data.pop()
    while len(data) > 0:
        last = data[-1]
        data.pop()
        for i in range(len(ordered)):
            if compare_lists(last, ordered[i]):
                ordered.insert(i, last)
                break
    return ordered

ordered = sort_packages(data)
a = ordered.index([[2]])+1
b = ordered.index([[6]])+1
assert a * b == 22464