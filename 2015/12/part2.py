import json

with open("input.txt") as file:
    data = file.read()

data = json.loads(data)

class balancing_book(object):

    def __init__(self):
        self.n = 0

    def scan_object(self, data):
        # the object is a dictionary, and contains red as a value, ignore it, if not, scan the object.
        if isinstance(data, dict):
            if "red" in data.values():
                pass
            else:
                for value in data.values():
                    self.scan_object(value)
        # if the object is a list, scan the object
        elif isinstance(data, list):
            for d in data:
                self.scan_object(d)
        # if the object is a string, do nothing
        elif isinstance(data, str):
            pass
        # if the object is an int, add the int to the sum of numbers.
        elif isinstance(data, int):
            self.n += data

book = balancing_book()
book.scan_object(data)
assert book.n == 65402

