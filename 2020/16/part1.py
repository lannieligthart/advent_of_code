import re
import numpy as np

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
print(tickets)


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

invalid_numbers = []
for t in tickets:
    for number in t:
        result = validate_number(number, rules)
        if result is not None:
            invalid_numbers.append(result)

print(sum(invalid_numbers))
