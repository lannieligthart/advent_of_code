import re

with open("input.txt") as file:
    data = file.read()

data = data.split("\n")

len1 = 0
len2 = 0
len3 = 0

for d in data:
    # part 1
    # length of uninterpreted string (counting outside quotes)
    len1 += len(d)
    # length of interpreted string (not counting outside quotes)
    len2 += len(bytes(d, "utf-8").decode("unicode_escape"))-2
    # part 2
    # add outside quotes to len (2), and for each quote and backslash, add 1 character
    n_quote = len(re.findall(r'\"', d))
    n_backslash = len(re.findall(r'\\', d))
    len3 += (len(d) + 2 + n_quote + n_backslash)

assert len1 - len2 == 1333
assert len3 - len1 == 2046
