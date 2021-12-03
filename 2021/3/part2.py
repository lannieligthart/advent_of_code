import AoC_tools.aoc_tools as aoc

data = aoc.lines2list("C:/Users/Admin/SURFdrive/Code/advent_of_code/2021/3/testinput.txt")

"""
life support rating = oxygen generator rating * CO2 scrubber rating

start with the full list of binary numbers from your diagnostic report and consider just the first bit
Keep only numbers selected by the bit criteria
If you only have one number left, stop; this is the rating value for which you are searching

Bit criteria:
oxygen generator rating: most common value
CO2 scrubber rating: least common value
If 0 and 1 are equally common, keep values with a 0 in the position being considered. 

"""

def get_most_common(data, i, reverse=False):
    count = 0
    for line in data:
        count += int(line[i])
    if count > len(data)/2:
        if not reverse:
            return 1
        else:
            return 0
    elif count < len(data)/2:
        if not reverse:
            return 0
        else:
            return 1
    else:
        return None


def filter(data, crit, pos, sel):
    if crit is not None:
        newdata = [line for line in data if line[pos] == str(crit)]
    elif crit is None:
        newdata = [line for line in data if line[pos] == str(sel)]
    return newdata


# oxygen generator rating
data = aoc.lines2list("C:/Users/Admin/SURFdrive/Code/advent_of_code/2021/3/input.txt")
n = len(data[0])
for i in range(n):
    crit = get_most_common(data, i)
    data = filter(data, crit, i, 1)
    print(data)
    if len(data) == 1:
        break
ogr = int(data[0], 2)
print(ogr)

# CO2 scrubber rating

data = aoc.lines2list("C:/Users/Admin/SURFdrive/Code/advent_of_code/2021/3/input.txt")
n = len(data[0])
for i in range(n):
    crit = get_most_common(data, i, reverse=True)
    data = filter(data, crit, i, 0)
    print(data)
    if len(data) == 1:
        break

csr = int(data[0], 2)
print(csr)

result = ogr * csr
print(result)

assert result == 903810