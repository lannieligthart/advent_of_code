import AoC_tools.aoc_tools as aoc
t = aoc.start()
data = aoc.lines2list("input.txt")
input_values = [line.split(" | ")[0] for line in data]
output_values = [line.split(" | ")[1] for line in data]

def run(input_line):
    input = [''.join(sorted(i)) for i in input_values[input_line].split()]
    output = [''.join(sorted(i)) for i in output_values[input_line].split()]

    numbers = {}
    for digit in input:
        if len(digit) == 7:
            numbers[8] = digit
        elif len(digit) == 2:
            numbers[1] = digit
        elif len(digit) == 4:
            numbers[4] = digit
        elif len(digit) == 3:
            numbers[7] = digit

    # 0, 9 en 6 heben len(6). 6 is de enige die niet beide elementen van 1 in zich heeft.
    len6 = [i for i in input if len(i) == 6]

    for s in len6:
        for char in numbers[1]:
            if char not in s:
                numbers[6] = s
                len6.remove(s)

    # 0 en 9 verschillen in d/e. In 4 zit alleen d maar niet e.
    # dus degene die niet volledig overlapt met 4 in de letter die verschilt, is 0.
    x = len6[0]
    y = len6[1]
    dif = []
    for char in x:
        if not char in y:
            dif.append(char)
    for char in y:
        if not char in x:
            dif.append(char)

    letter_not_in_4 = [l for l in dif if l not in numbers[4]]
    for s in len6:
        if letter_not_in_4[0] in s:
            numbers[0] = s
        elif letter_not_in_4[0] not in s:
            numbers[9] = s

    # 2 is degene van len(5) die niet volledig overlapt met 9.
    len5 = [i for i in input if len(i) == 5]
    for s in len5:
        for char in s:
            if char not in numbers[9]:
                numbers[2] = s
                len5.remove(s)

    # 3 en 5 zijn nu over. 3 is degene die niet volledig overlapt met 6.
    for s in len5:
        for char in s:
            if char not in numbers[6]:
                numbers[3] = s
                len5.remove(s)

    # 5 is degene die overblijft.
    numbers[5] = len5[0]
    result = ''
    for o in output:
        for key, value in numbers.items():
            if o == value:
                result += str(key)
                break
    return result

sum = 0
for i in range(len(data)):
    sum += int(run(i))
print(sum)
assert sum == 1019355
aoc.end(t)
