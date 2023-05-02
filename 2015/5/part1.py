
def contains_3_vowels(txt):
    n = 0
    for char in txt:
        if char in 'aeiou':
            n += 1
    if n >= 3:
        return True
    else:
        return False

def contains_repeat(txt):
    previous = None
    for char in txt:
        if char == previous:
            return True
        previous = char
    return False

def contains_forbidden_string(txt):
    forbidden = ['ab', 'cd', 'pq', 'xy']
    for f in forbidden:
        if f in txt:
            return True
    return False

def is_nice(txt):
    if contains_3_vowels(txt) and contains_repeat(txt) and not contains_forbidden_string( txt):
        return True
    else:
        return False

with open("input.txt") as file:
    data = file.read().split("\n")

n_nice = 0

for d in data:
    if is_nice(d):
        n_nice += 1

assert n_nice == 236