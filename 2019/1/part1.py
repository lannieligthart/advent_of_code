import math

with open('C:/Users/Admin/Documents/Code/advent_of_code/2019/1/input.txt') as f:
    data = f.read().splitlines()

def calculate_fuel(mass):
    result = math.floor(mass/3) - 2
    return result

mod_fuel = 0

for d in data:
    f = calculate_fuel(int(d))
    mod_fuel += f

# fuel needed for the modules
print("fuel for modules:", mod_fuel)


