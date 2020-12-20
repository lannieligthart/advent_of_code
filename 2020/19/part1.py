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

    def parse_rule(input_line):
        input_line = input_line.split(": ")
        index = int(input_line[0])
        if not "|" in input_line[1]:
            rule = input_line[1]
        elif "|" in input_line[1]:
            rule = "( " + input_line[1]+ " )"
        rule = rule.replace('"', '')
        return (index, rule)

    ruledict = {}
    for rule in input_lines:
        index, rule = parse_rule(rule)
        ruledict[index] = rule
    return ruledict

def add_brackets(ruledict):
    i = 0
    while True:
        for number, value in ruledict.items():
            values = value.split(" ")
            for i in range(len(values)):
                # replace each item in the list by its translation
                if values[i] in ["|", "a", "b", "(", ")"]:
                    values[i] = values[i]
                elif int(values[i]) in ruledict:
                    if "|" in ruledict[int(values[i])]:
                        values[i] = "( "+ ruledict[int(values[i])] + " )"
            ruledict[number] = " ".join(values)
            i += 1
            if i > 3:
                return ruledict

def translate(ruledict):
    dictcopy = ruledict.copy()
    while True:
        for number, value in ruledict.items():
            values = value.split(" ")
            for i in range(len(values)):
                # replace each item in the list by its translation
                if values[i] in ["|", "a", "b", "(", ")"]:
                    values[i] = values[i]
                elif int(values[i]) in ruledict:
                    values[i] = ruledict[int(values[i])]
            ruledict[number] = " ".join(values)
        if ruledict == dictcopy:
            return ruledict
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
ruledict = add_brackets(ruledict)
ruledict = translate(ruledict)

for rule, value in ruledict.items():
    ruledict[rule] = ruledict[rule].split(" ")
    ruledict[rule] = "".join(ruledict[rule])

print("after translation:")
for key, value in ruledict.items():
    print(key, value)

valid_messages = 0
for m in messages:
    if validate(m):
        valid_messages += 1

print("n valid:", valid_messages)

assert valid_messages == 200