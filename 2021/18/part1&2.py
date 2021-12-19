from math import ceil, trunc
from itertools import combinations
import re
import AoC_tools.aoc_tools as aoc

# part 1 was easy, part 2 was a fucking nightmare.
# not my proudest work but I'm glad I finished it at least.

def convert(string):
    numbers = []
    levels = []
    level = 0
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    i = 0
    while True:
        if string[i] == '[':
            level += 1
            i += 1
        elif string[i] == ']':
            level -= 1
            i += 1
        elif string[i] == ',':
            i += 1
        elif string[i] in num:
            if not string[i+1] in num:
                numbers.append(int(string[i]))
                levels.append(level)
                i += 1
            elif string[i+1] in num:
                numbers.append(int(string[i:i+2]))
                levels.append(level)
                i += 2
        if i == len(string):
            break
    return(numbers, levels, string)


def add(som1, som2):
    #print("adding:")
    numbers1 = som1[0]
    levels1 = som1[1]
    full_string1 = som1[2]
    numbers2 = som2[0]
    levels2 = som2[1]
    full_string2 = som2[2]
    for i in range(len(levels1)):
        levels1[i] += 1
    for i in range(len(levels2)):
        levels2[i] += 1
    levels1.extend(levels2)
    numbers1.extend(numbers2)
    levels = levels1
    numbers = numbers1
    fullstring = "[" + full_string1 + "," + full_string2 + "]"
    som = (numbers, levels, fullstring)
    # if there's something to explode, explode the first thing there is to explode. If not, continue to check if
    # anything needs to be split.
    while 5 in som[1] or any(n >= 10 for n in som[0]):
        while 5 in som[1]:
            som = explode(som)
            #print(som)
        if any(n >= 10 for n in som[0]):
            som = split(som)
        #print(som)
    return som


def explode(som):
    #print("exploding")
    numbers = som[0]
    levels = som[1]
    fullstring = som[2]
    for i in range(len(levels)):
        if levels[i] == 5:
            # splits de arrays op in 3 delen.
            # eerste deel (als het bestaat) krijgt getal 1 met level 5 bij het laatste getal, 2e deel (als het bestaat)
            # krijgt getal 2 met level 4 bij het eerste getal.
            # het middelste deel valt weg.
            numbers1 = numbers[:i]
            numbers2 = numbers[i+2:]
            levels1 = levels[:i]
            levels2 = levels[i+2:]
            # dit zijn de getallen die opgeteld moeten worden bij de positie ervoor of erna
            ex1 = numbers[i]
            ex2 = numbers[i+1]
            if len(numbers1) > 0:
                numbers1[-1] += ex1
            if len(numbers2) > 0:
                numbers2[0] += ex2
            numbers1.append(0)
            numbers1.extend(numbers2)
            levels1.append(4)
            levels1.extend(levels2)
            # now adjust the fullstring
            # get the indices of all numbers
            numbers = numbers1
            levels = levels1
            #find all number indices
            n_indices = []
            num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            count = 0
            while True:
                if fullstring[count] in num:
                    start = count
                    if fullstring[count + 1] not in num:
                        end = count + 1
                        count += 1
                    elif fullstring[count + 1] in num:
                        end = count + 2
                        count += 2
                    n_indices.append((start, end))
                elif fullstring[count] not in num:
                    count += 1
                if count == len(fullstring):
                    break
            # n_indices bevat nu een lijst van de indices van alle getallen in de oorspronkelijke string.
            # get start position in string of the index of the first number to remove
            start = n_indices[i][0]
            # get end position in string of the index of the first number to remove
            end = n_indices[i + 1][1]
            fs1 = fullstring[:start-1]
            fs2 = fullstring[end+1:]
            fsnew = fs1 + '0' + fs2
            fsnew = replace(numbers, fsnew)
            som = numbers, levels, fsnew
            if not som[0] == convert(som[2])[0]:
                print(som[0])
                print(convert(som[2])[0])
                raise AssertionError("error in explode")
            return(som)

    return(som)

def replace(numbers, string):
    data = [str(n) for n in numbers]
    string = re.sub(r"[0-9]+", "{}", string)
    string = (string).format(*data)
    return string

def split(som):
    #print("Splitting")
    numbers = som[0]
    levels = som[1]
    fullstring = som[2]
    for i in range(len(numbers)):
        if numbers[i] > 9:
            numbers1 = numbers[:i]
            numbers2 = numbers[i+1:]
            levels1 = levels[:i]
            levels2 = levels[i+1:]
            n1 = int(trunc(numbers[i]/2))
            n2 = int(ceil(numbers[i]/2))
            numbers1.append(n1)
            numbers1.append(n2)
            numbers1.extend(numbers2)
            levels1.append(levels[i] + 1)
            levels1.append(levels[i] + 1)
            levels1.extend(levels2)
            # find index of the first number > 9:
            num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            for i in range(len(fullstring)):
                if fullstring[i] in num and fullstring[i+1] in num and int(fullstring[i:i+2]) > 9:
                    idx = i # dit is de index van de eerste digit (er zijn er altijd 2)
                    break
            try:
                fs1 = fullstring[:idx]
            except Exception as e:
                print(fullstring)
                print(fullstring[i:i+2])
                raise e
            fs2 = fullstring[idx+2:]
            fsnew = fs1 + '[' + str(n1) + ',' + str(n2) + ']' + fs2
            som = (numbers1, levels1, fsnew)
            if not som[0] == convert(som[2])[0]:
                print(som[0])
                print(convert(som[2])[0])
                raise AssertionError("error in split")
            return(som)
    return(som)

def mag2(result):
    result[0] = result[0] * 3
    result[1] = result[1] * 2
    return result[0] + result[1]

def magnitude(result):
    while True:
        if isinstance(result, int):
            return result
        elif isinstance(result[0], int) and isinstance(result[1], int):
            result = mag2(result)
        else:
            if isinstance(result[0], list):
                result[0] = magnitude(result[0])
            if isinstance(result[1], list):
                result[1] = magnitude(result[1])


## TESTS ###

# som = convert('[[[[[9,8],1],2],3],4]')
# assert(explode(som)[2] == '[[[[0,9],2],3],4]')
#
# som = convert('[7,[6,[5,[4,[3,2]]]]]')
# assert(explode(som)[2] == '[7,[6,[5,[7,0]]]]')
#
# som = convert('[[6,[5,[4,[3,2]]]],1]')
# assert(explode(som)[2] == '[[6,[5,[7,0]]],3]')
#
# som = convert('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]')
# assert(explode(som)[2] == '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')
#
# som = convert('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')
# assert(explode(som)[2] == '[[3,[2,[8,0]]],[9,[5,[7,0]]]]')
#
# som = convert('[[[[0,7],4],[[7,8],[0,13]]],[1,1]]')
# assert split(som)[2] == '[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]'
#
# som1 = convert('[[[[4,3],4],4],[7,[[8,4],9]]]')
# som2 = convert('[1,1]')
# result = add(som1, som2)
# print(result)
# assert(result[2] == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')

# som = convert('[[[[4,0],[5,4]],[[7,0],[15,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]')
# print(som)
#
# som = convert('[[[[4,0],[5,4]],[[0,[7,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]')
# print(explode(som))

# som = (convert('[[[[4,0],[5,4]],[[7,0],[15,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]'))
# assert explode(som)[0] == [4, 0, 5, 4, 7, 0, 15, 5, 10, 0, 11, 3, 6, 3, 8, 8]

# data = aoc.lines2list("testinput.txt")
# som = add(convert(data[0]), convert(data[1]))
# print(som)
#
# for i in range(2, len(data)):
#     som = add(som, convert(data[i]))
#     print(som)
#
# assert som[2] == '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'

data = aoc.lines2list("input.txt")

# part 1
som = add(convert(data[0]), convert(data[1]))

for i in range(2, len(data)):
    som = add(som, convert(data[i]))

assert som[2] == '[[[[7,7],[7,0]],[[7,8],[8,8]]],[6,9]]'
result = eval(som[2])
magn = (magnitude(result))
print(magn)
assert magn == 2541

# part 2
combos = [c for c in combinations(data, 2)]
magnitudes = []

for i in range(len(combos)):
    som1 = convert(combos[i][0])
    som2 = convert(combos[i][1])
    som = add(som1, som2)
    result = eval(som[2])
    magnitudes.append(magnitude(result))

for i in range(len(combos)):
    som1 = convert(combos[i][0])
    som2 = convert(combos[i][1])
    som = add(som2, som1)
    result = eval(som[2])
    magnitudes.append(magnitude(result))

print(max(magnitudes))
assert max(magnitudes) == 4647