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
                right[i] = [right[i]]
                result = compare_lists(left[i], right[i])
            elif isinstance(left[i], int) and isinstance(right[i], list):
                left = [left[i]]
                result = compare_lists(left, right[i])
            if result:
                return True
            elif result is False:
                return False
    except IndexError:
        if len(left) < len(right):
            return True
        elif len(left) > len(right):
            return False

data = aoc.read_input("input.txt", "\n\n", "\n")

total = 0
for i in range(len(data)):
    if compare_lists(data[i][0], data[i][1]):
        total += i+1

assert total == 6428