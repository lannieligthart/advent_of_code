import re

with open("input.txt") as file:
    data = file.read()

numbers = re.findall("[0-9\-]+", string=data)
numbers = [int(n) for n in numbers]

assert sum(numbers) == 111754