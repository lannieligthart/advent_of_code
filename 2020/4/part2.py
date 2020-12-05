import re

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

def validate_passport(passport):
    # all fields except cid
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = True
    for f in fields:
        if not f in passport:
            valid = False
    return valid

def check_4digits(value, min, max):
    try:
        value = int(value)
    except ValueError:
        return False
    if isinstance(value, int) and value >= min and value <= max:
        return True
    else:
        return False

def validate_byr(value):
    return check_4digits(value, 1920, 2002)

def validate_iyr(value):
    return check_4digits(value, 2010, 2020)

def validate_eyr(value):
    return check_4digits(value, 2020, 2030)

def validate_hgt(value):
    unit = value[-2:]
    try:
        value = int(value[:-2])
    except ValueError:
        return False
    if unit == 'cm' and value >= 150 and value <= 193:
        return True
    elif unit == 'in' and value >= 59 and value <= 76:
        return True
    else:
        return False

def validate_hcl(value):
    if value[0] == "#" and (re.search("[0-9a-f]{6}", value)):
        return True
    else:
        return False

def validate_ecl(value):
    if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    else:
        return False

def validate_pid(value):
    if len(value) == 9 and (re.search("[0-9]{9}", value)):
        return True
    else:
        return False

n_valid = 0
for p in passports:
    if (validate_passport(p)):
        n_valid += 1

print("Number of valid passports according to first check:", n_valid)

assert(validate_hgt("60in")) is True
assert(validate_hgt("190cm")) is True
assert(validate_hgt("190in")) is False
assert(validate_hgt("190")) is False

assert(validate_hcl("#123abc")) is True
assert(validate_hcl("#123abz")) is False
assert(validate_hcl("123abc")) is False

assert(validate_ecl("brn")) is True
assert(validate_ecl("wat")) is False

assert(validate_pid("000000001")) is True
assert(validate_pid("0123456789")) is False

def validate_passport_strict(passport):
    if not validate_passport(passport):
        return False
    else:
        if not validate_byr(passport['byr']):
            return False
        elif not validate_iyr(passport['iyr']):
            return False
        elif not validate_eyr(passport['eyr']):
            return False
        elif not validate_hgt(passport['hgt']):
            return False
        elif not validate_hcl(passport['hcl']):
            return False
        elif not validate_ecl(passport['ecl']):
            return False
        elif not validate_pid(passport['pid']):
            return False
        else:
            return True

n_valid_strict = 0
for p in passports:
    if validate_passport_strict(p):
        #print("Valid!")
        n_valid_strict += 1
    elif not validate_passport_strict(p):
        #print("Invalid!")
        pass

assert(n_valid_strict) == 224

