
def contains_repeat(txt):
    for i in range(len(txt)-1):
        seq = txt[i:i+2]
        rem1 = txt[0:i]
        rem2 = txt[i+2:]
        if seq in rem1 or seq in rem2:
            return True
    return False

def contains_repeat2(txt):
    for i in range(len(txt)-2):
        if txt[i] == txt[i+2]:
            return True
    return False

def is_nice(txt):
    if contains_repeat(txt) and contains_repeat2(txt):
        return True
    else:
        return False

with open("input.txt") as file:
    data = file.read().split("\n")
n_nice = 0

for d in data:
    if is_nice(d):
        n_nice += 1

assert n_nice == 51