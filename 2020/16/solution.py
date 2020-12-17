from dataclasses import dataclass


def parse_input_file():
    with open("input.txt", "r") as file:
        return [i.strip() for i in file.read().split('\n\n')]


@dataclass
class FieldRanges:
    name: str
    min1: int
    max1: int
    min2: int
    max2: int


def part_1():
    input = parse_input_file()
    field_ranges = []

    for field in [i for i in input[0].splitlines()]:
        ranges = field.split(':')[1].strip().split('or')
        range1 = ranges[0].split('-')
        range2 = ranges[1].split('-')
        field_ranges.append(
            FieldRanges(field.split(':')[0], int(range1[0]), int(range1[1]), int(range2[0]), int(range2[1])))

    nearby_tickets_fields = [j for i in input[2].splitlines()[1:] for j in i.split(',')]
    invalid_sum = 0

    for field in nearby_tickets_fields:
        for r in field_ranges:
            if r.min1 <= int(field) <= r.max1 or r.min2 <= int(field) <= r.max2:
                break
        else:
            invalid_sum += int(field)

    print(invalid_sum)


def part_2():
    input = parse_input_file()
    field_ranges = []
    potential_field_indices = {}
    fields = [i for i in input[0].splitlines()]

    for field in fields:
        ranges = field.split(':')[1].strip().split('or')
        range1 = ranges[0].split('-')
        range2 = ranges[1].split('-')
        field_name = field.split(':')[0]
        potential_field_indices[field_name] = [i for i in range(len(fields))]
        field_ranges.append(FieldRanges(field_name, int(range1[0]), int(range1[1]), int(range2[0]), int(range2[1])))

    your_ticket = input[1].splitlines()[1].split(',')
    tickets = [i.split(',') for i in input[2].splitlines()[1:]]
    valid_tickets = tickets.copy()

    for ticket in tickets:
        for field in ticket:
            for r in field_ranges:
                if r.min1 <= int(field) <= r.max1 or r.min2 <= int(field) <= r.max2:
                    break
            else:
                valid_tickets.remove(ticket)
    for ticket in valid_tickets:
        for ix, field in enumerate(ticket):
            for r in field_ranges:
                if not (r.min1 <= int(field) <= r.max1 or r.min2 <= int(field) <= r.max2):
                    if ix in potential_field_indices[r.name]:
                        potential_field_indices[r.name].remove(ix)

    to_remove = []
    done = False

    while not done:
        for key, value in potential_field_indices.items():
            for elem in to_remove:
                if key != elem[0] and elem[1] in value:
                    value.remove(elem[1])
            if len(value) == 1:
                if (key, value[0]) not in to_remove:
                    to_remove.append((key, value[0]))
                    if len(to_remove) == len(potential_field_indices):
                        done = True
                        break
    departure_values_multiplied = 1

    for key, value in potential_field_indices.items():
        if 'departure' in key:
            departure_values_multiplied *= int(your_ticket[value[0]])

    print(departure_values_multiplied)


### Part 1 ###
part_1()

### Part 2 ###
part_2()