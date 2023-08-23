
def add_one(char):
    # increase a letter by one
    newchar = ord(char) + 1
    if newchar - 97 == 26:
        newchar = 97
    newchar = chr(newchar)
    #print(newchar)
    return newchar

def increment(pw):
    # increment the password string by one, as if it were a number.
    pw = pw[::-1]
    new_pw = ""
    pos = 0
    # increase last character until you reach z, then increase the one before.
    while True:
        char = pw[pos]
        char = add_one(char)
        # if the new char is an a we have to move to the next character and the loop repeats
        if char == "a":
            new_pw += char
            pos += 1
            if pos == len(pw):
                print(new_pw)
                return new_pw[::-1]
        # if the new char is not an a we're done.
        else:
            new_pw += char
            new_pw += pw[pos + 1:]
            return new_pw[::-1]

def req1(pw):
    # password should have one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz.
    for i in range(len(pw)-2):
        if ord(pw[i]) - ord(pw[i + 1]) == -1 and ord(pw[i + 1]) - ord(pw[i + 2]) == -1:
            return True
    return False

def req2(pw):
    # password cannot contain i, o or l.
    for i in range(len(pw)):
        if pw[i] in ["i", "o", "l"]:
            return False
    return True

def req3(pw):
    # Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
    chars = set()
    for i in range(len(pw)-1):
        if pw[i] == pw[i + 1]:
            chars.add(pw[i])
            if len(chars) == 2:
                return True
    return False

def get_next_pw(pw):
    # determine Santa's next password, taking the password requirements into account.
    while True:
        pw = increment(pw)
        if req1(pw) and req2(pw) and req3(pw):
            print(pw)
            return pw

part1 = get_next_pw("hxbxwxba")
part2 = get_next_pw(part1)

assert part1 == "hxbxxyzz"
assert part2 == "hxcaabcc"