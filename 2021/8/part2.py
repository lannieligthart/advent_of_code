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
        if not set(numbers[1]).issubset(set(s)):
            numbers[6] = s
            len6.remove(s)
            break

    # 0 en 9 verschillen in d/e. In 4 zit alleen d maar niet e.
    # dus degene die niet volledig overlapt met 4 in de letter die verschilt, is 0, de ander is 9.
    dif1 = set(len6[0]) - set(len6[1])
    dif2 = set(len6[1]) - set(len6[0])
    dif = list(dif1.union(dif2))

    # bepaal welke van dif er niet in 4 voorkomt (kan er maar 1 zijn dus wordt een list van len 1).
    not_in_4 = [l for l in dif if l not in numbers[4]][0]
    for s in len6:
        if not_in_4 in s:
            numbers[0] = s
        elif not_in_4 not in s:
            numbers[9] = s

    # 2 is degene van len(5) die niet volledig overlapt met 9.
    len5 = [i for i in input if len(i) == 5]
    for s in len5:
        if not set(s).issubset(set(numbers[9])):
            numbers[2] = s
            len5.remove(s)
            break

    # 3 en 5 zijn nu over. 3 is degene die niet volledig overlapt met 6.
    for s in len5:
        if not set(s).issubset(set(numbers[6])):
            numbers[3] = s
            len5.remove(s)
            break

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
