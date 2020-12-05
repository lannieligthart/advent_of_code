import math

with open('C:/Users/Admin/Documents/Code/advent_of_code/2019/1/input.txt') as f:
    data = f.read().splitlines()

def calculate_fuel(mass):
    # calculate fuel for module
    fuel_for_module = math.floor(mass/3) - 2
    return(fuel_for_module)

def calculate_total_fuel(data):
    total_fuel = 0
    for d in data:
        # calculate fuel needed for module
        fuel_for_module = calculate_fuel(int(d))

        # now calculate fuel needed for the fuel for this module
        fuel_needing_fuel = fuel_for_module
        extra_fuel = 0
        while fuel_needing_fuel > 0:
            # calculate fuel needed for remaining fuel
            f = calculate_fuel(fuel_needing_fuel)
            print(f)
            # set the new amount of remaining fuel to this value
            fuel_needing_fuel = f
            # if the amount needed is > 0, add it to the amount of extra fuel needed
            if f >= 0:
                extra_fuel += f
                print(extra_fuel)
        total_fuel_module = fuel_for_module + extra_fuel
        total_fuel += total_fuel_module

    return total_fuel

fuel_needed = calculate_total_fuel(data)
print(fuel_needed)
