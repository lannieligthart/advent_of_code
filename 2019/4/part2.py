import re

min = 171309
max = 643603

def six_digits(pw):
    if re.search("[0-9]{6}", pw):
        return True
    else:
        return False

def len_six(pw):
    if len(pw) == 6:
        return True
    else:
        return False

def two_adjacent_strict(pw):
    # at least 2 but not 3 adjacent
    # first two the same but not the third
    if pw[0] == pw[1] and pw[1] != pw[2]:
        return True
    # two the same but not the ones before and after
    for i in range(1,4):
        if pw[i] == pw[i+1] and pw[i+1] != pw[i+2] and pw[i] != pw[i-1]:
            return True
    # last two the same but not the one before
    if pw[4] == pw[5] and pw[4] != pw[3]:
        return True
    else:
        return False

def no_decrease(pw):
    for i in range(1, len(pw)):
        if int(pw[i]) < int(pw[i - 1]):
            return False
    return True

def potential_pw(pw):
    if six_digits(pw) and len_six(pw) and two_adjacent_strict(pw) and no_decrease(pw):
        return True
    else:
        return False

count = 0
for pw in range(min, max+1):
    if potential_pw(str(pw)):
        count += 1

print(count)

assert count == 1111
