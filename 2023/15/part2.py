
import re

with open("input.txt") as file:
    data = file.read()

data = data.split(",")

class Lens(object):

    def __init__(self, label, op):
        self.label
        self.op


def hash(data):
    value = 0
    for char in data:
        value += ord(char)
        value *= 17
        value = value % 256
    return value

def get_box(label):
    return hash(label)

def add(boxes, box, label, instr):
    # check if lens is already in boxes[box]
    b = boxes[box]
    # if lens is already in box, replace
    for l in range(len(b)):
        if re.split(r'[=-]', b[l])[0] == label:
            boxes[box][l] = instr
            return
    # if lens is not in box yet, append it
    boxes[box].append(instr)

def remove(boxes, box, label):
    b = boxes[box]
    for l in range(len(b)):
        if label.split("-")[0] == b[l].split("-")[0]:
            del b[l]
            return
        elif label.split("-")[0] == b[l].split("=")[0]:
            del b[l]
            return


def calc(boxes):
    total = 0
    for key, value in boxes.items():
        for i in range(len(value)):
            boxnr = key + 1
            slot = i + 1
            fl = int(re.split('[=-]', value[i])[1])
            total += boxnr*slot*fl
    return total

boxes = {i: [] for i in range(256)}

for instr in data:
    label, focal_len = re.split(r'[=-]', instr)
    op = re.findall(r'[=-]', instr)[0]
    box = hash(label)

    if op == '=':
        add(boxes, box, label, instr)
    elif op == '-':
        remove(boxes, box, label)

assert calc(boxes) == 267372

