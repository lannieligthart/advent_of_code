data = "1113122113"
#data = "211"


def look_say(data):
    newdata = ''
    i = 0
    # set current digit and n
    digit = data[i]
    n = 1
    while True:
        # indien geen verandering:
        try:
            if data[i + 1] == data[i]:
                n += 1
                i += 1
            # indien we switchen naar een andere digit:
            elif data[i + 1] != data[i]:
                newdata += str(n)
                newdata += digit
                digit = data[i + 1]
                i += 1
                n = 1
                #print(newdata)
        except IndexError:
            newdata += str(n)
            newdata += digit
            return newdata

# part 1

data = "1113122113"
round = 0
while round < 40:
    #print("round", round)
    data = look_say(data)
    round += 1

assert len(data) == 360154

# part 2

data = "1113122113"
round = 0
while round < 50:
    #print("round", round)
    data = look_say(data)
    round += 1

assert len(data) == 5103798