with open('input.txt') as f:
    passports = f.read().split("\n\n")

# read passport data into dictionaries
for i in range(len(passports)):
    passports[i] = passports[i].replace("\n", " ")
    passports[i] = passports[i].split(" ")
    passport = passports[i]
    d = {}
    for entry in passport:
        tmp = entry.split(":")
        if entry != '':
            d[tmp[0]] = tmp[1]
    passports[i] = d

print(passports)


def validate_passport(passport):
    # all fields except cid
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = True
    for f in fields:
        if not f in passport:
            valid = False
    return valid

n_valid = 0
for p in passports:
    if (validate_passport(p)):
        n_valid += 1

print(n_valid)




