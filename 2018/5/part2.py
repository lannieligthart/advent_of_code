with open("input.txt") as file:
    polymer = file.read()


def react(polymer):
    while True:
        l1 = len(polymer)
        for i in range(len(polymer) - 1):
            char1 = polymer[i]
            char2 = polymer[i + 1]
            if char1.lower() == char2.lower() and char1 != char2:
                polymer = polymer.replace(char1 + char2, "")
                l2 = len(polymer)
                break
        if l2 == l1:
            return polymer


# make a copy of the input to reset it after each run
polycopy = polymer

# arrays of all lower and upper case letters
lc = [chr(i) for i in range(97, 97 + 26)]
uc = [chr(i) for i in range(65, 65 + 26)]


# remove all lower and uppercase occurrences of a character from the string, react the remaining polymer and save length
# of result

results = []

for i in range(26):
    polymer = polymer.replace(lc[i], "")
    polymer = polymer.replace(uc[i], "")
    result = react(polymer)
    if result is not None:
        results.append(len(result))
    # reset polymer before moving on to next letter
    polymer = polycopy

assert min(results) == 5094
