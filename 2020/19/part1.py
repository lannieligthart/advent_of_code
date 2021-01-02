import re

with open('input.txt') as f:
    data = f.read().split("\n")

input_lines = []
messages = []

line = 0
while not data[line] == '':
    input_lines.append(data[line])
    line += 1
while not line >= len(data)-1:
    line += 1
    messages.append(data[line])


def parse_rules(input_lines):
    ruledict = {}
    for line in input_lines:
        line = line.split(": ")
        index = int(line[0])
        if "|" in line[1]:
            rule = "( " + line[1]+ " )"
        else:
            rule = line[1]
        rule = rule.replace('"', '')
        ruledict[index] = rule
    return ruledict

def translate(ruledict):
    dictcopy = ruledict.copy()
    while True:
        values = ruledict[0].split(" ")
        for i in range(len(values)):
            # replace each item in the list by its translation
            if not values[i].isdigit():
                values[i] = values[i]
            elif int(values[i]) in ruledict:
                values[i] = ruledict[int(values[i])]
        ruledict[0] = " ".join(values)

        # for key, value in ruledict.items():
        #     values = value.split(" ")
        #     for i in range(len(values)):
        #         # replace each item in the list by its translation
        #         if not values[i].isdigit():
        #             values[i] = values[i]
        #         elif int(values[i]) in ruledict:
        #             values[i] = ruledict[int(values[i])]
        #     ruledict[key] = " ".join(values)
        # once there are no more changes, convert 0 to regex:
        if ruledict == dictcopy:
            regex = ruledict[0]
            regex = "^" + "".join(regex.split(" ")) + "$"
            return regex
        dictcopy = ruledict.copy()


def validate(message):
    rule = ruledict[0]
    regex = "^" + rule + "$"
    if re.match(regex, message):
        return True
    else:
        return False

ruledict = parse_rules(input_lines)
# we need two rounds of translation (for the real input we need 4
regex = translate(ruledict)
print(regex)

valid_messages = 0
for m in messages:
    if re.match(regex, m):
        valid_messages += 1

print("n valid:", valid_messages)

assert valid_messages == 200