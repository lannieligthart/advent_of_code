with open('C:/Users/Admin/Documents/Code/advent_of_code/1/input.txt') as f:
    input = f.read().splitlines()
    input = [int(i) for i in input]
    input.sort()
    print(input)

def get_product(input):
    for i in range(len(input)):
        for j in (range(len(input))):
            n1 = input[i]
            n2 = input[j]
            for k in (range(len(input))):
                n3 = input[k]
                if n1 + n2 + n3 == 2020:
                    product = n1 * n2 * n3
                    print(n1, n2, n3)
                    return product

print(get_product(input))