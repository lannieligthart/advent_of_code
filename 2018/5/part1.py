input = "dabAcCaCBAcCcaDA"
with open("input.txt") as file:
    input = file.read()



while True:
    l1 = len(input)
    print(l1)
    for i in range(len(input) - 1):
        char1 = input[i]
        char2 = input[i + 1]
        if char1.lower() == char2.lower() and char1 != char2:
            input = input.replace(char1 + char2, "")
            print("removed", char1 + char2)
            l2 = len(input)
            print(l2)
            break
    if l2 == l1:
        break

print(l2)

assert l2 == 11108

