with open("input.txt") as file:
    data = file.read().split("\n")

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def extract_numbers(s):
    # loop through the string. At each position, test whether the character is a digit, or the beginning of a
    # "word-digit". Append all to a list and return the first and last.
    result = []
    for i in range(len(s)):
        # digits
        if s[i].isdigit():
            result.append(int(s[i]))
        # words
        else:
            for n in numbers:
                if s[i:].startswith(n):
                    idx = numbers.index(n)
                    result.append(idx + 1)
    return (result[0], result[-1])

result = 0

for line in data:
    d1, d2 = extract_numbers(line)
    result += int(str(d1) + str(d2))

assert result == 53894
