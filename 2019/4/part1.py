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

def two_adjacent(pw):
    for i in range(1,len(pw)-1):
        if pw[i] == pw[i-1]:
            return True
    return False

def no_decrease(pw):
    for i in range(1, len(pw)):
        if int(pw[i]) < int(pw[i - 1]):
            return False
    return True

def potential_pw(pw):
    if six_digits(pw) and len_six(pw) and two_adjacent(pw) and no_decrease(pw):
        return True
    else:
        return False

assert potential_pw('111111') == True
assert potential_pw('223450') == False
assert potential_pw('123789') == False

count = 0
for pw in range(min, max+1):
    if potential_pw(str(pw)):
        count += 1

print(count)