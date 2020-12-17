import re
import numpy as np
from functools import reduce

with open('input.txt') as f:
    data = f.read().split("\n")

print(data)

def parse_rule(rule):
    new_rule = []
    for i in range(len(rule)):
        rule[i] = rule[i].split("-")
        new_rule.append(np.arange(int(rule[i][0]), int(rule[i][1])+1))
    return new_rule

def parse_ticket(ticket):
    ticket = ticket.split(",")
    new_ticket = []
    for t in ticket:
        new_ticket.append(int(t))
    return new_ticket

def extract_rules(data):
    rules = []
    regex = "[0-9]{1,}-[0-9]{1,}"
    for d in data:
        if re.search(regex, d):
            d = re.findall(regex, d)
            rules.append(parse_rule(d))
    return rules

i = 0
tickets = []
while data[i] != 'nearby tickets:':
    i += 1
while i < len(data)-1:
    i += 1
    tickets.append(parse_ticket(data[i]))
print("total n tickets:", len(tickets))


def check_rule(number, rule):
    # if number does not fall within either range, it is invalid for this rule
    if number not in rule[0] and number not in rule[1]:
        return False
    else:
        return True

def validate_number(number, rules):
    # to be valid, the number should pass at least one rule
    checks = []
    for rule in rules:
        checks.append(check_rule(number, rule))
    # if zero checks are passed, return the number as it is invalid
    if sum(checks) == 0:
        return number

rules = extract_rules(data)
valid_tickets = []
for t in tickets:
    invalid_numbers = []
    for number in t:
        result = validate_number(number, rules)
        if result is not None:
            invalid_numbers.append(result)
    if len(invalid_numbers) == 0:
        valid_tickets.append(t)

print("valid tickets:", len(valid_tickets))

fields = []
for d in data:
    if d == '':
        break
    fields.append(d.split(":")[0])
print(fields)

# loop per rule per veld alle tickets af en check of het veld steeds aan de checks voldoet.
# als dat niet zo is dan kan de rule niet bij dat veld horen.

possible_fields = []
for f in range(len(fields)):
    possible_fields.append(list(np.arange(0, len(fields))))

for f in range(len(fields)):
    for i in range(len(rules)):
        errors = []
        for t in valid_tickets:
            number = t[f]
            result = check_rule(number, rules[i])
            if not result:
                possible_fields[f].remove(i)

print(possible_fields)

matches = {}
while len(matches) < len(rules):
    for i in range(len(possible_fields)):
        value = possible_fields[i][0]
        if len(possible_fields[i]) == 1 and value not in matches.values():
            matches[fields[i]] = value
            print("value:", value)
            #        possible_fields.remove(possible_fields[i])
            for j in range(len(possible_fields)):
                if len(possible_fields[j]) > 1:
                    possible_fields[j].remove(value)
        print(possible_fields)

print(possible_fields)
print(fields)
print(matches)

for i in range(len(data)):
    if data[i] == 'your ticket:':
        my_ticket = parse_ticket(data[i+1])

print("my ticket:", my_ticket)

departure_numbers = {}

for key, value in matches.items():
    if 'departure' in key:
        departure_numbers[key] = my_ticket[value]

print("departure numbers:", departure_numbers)
print(reduce(lambda x, y: x*y, departure_numbers.values()))

#7067386090733 too high

# departure station moet 5 zijn?!