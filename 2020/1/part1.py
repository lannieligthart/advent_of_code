with open('testinput.txt') as f:
    input = f.read().splitlines()
    input = [int(i) for i in input]
    input.sort()
    print(input)


for i in range(len(input)):
    for j in reversed(range(len(input))):
        n1 = input[i]
        n2 = input[j]
        if n1 + n2 == 2020:
            product = n1 * n2
            print(n1, n2)
            break
        break


print(product)
