import time
startTime = time.time()

input = "12345678"

repseq = [0, 1, 0, -1]

output = []

# possible strategies:
# delete everything that multiplies by 0
# so something with the repeating sequence when input * 10000


def phase(input):
    result = []
    for n in range(1, len(input) + 1):
        print("N =", n)
        subresult = []
        for i in range(len(str(input))):
        #for i in range(8):
            # i represents position within the array of input numbers.
            # we need to adjust this position so as to map it to the repeat seq array.
            # this means every element in the first quarter gets a zero, second quarter gets 1, etc.
            element = int(str(input)[i])
            # divide by N to get the adjusted rs_i
            # correct for offset of 1 by adding 1 to i before division.
            rs_i = int((i+1)/n) % len(repseq)
            #print(str(element), str(repseq[rs_i]))
            tmp = element * repseq[rs_i]
            print("i" + str(i) + ") " + str(element) + "*" + str(repseq[rs_i]) + " = " + str(tmp))
            subresult.append(tmp)
        elements2sum = [str(x)[-1] for x in subresult]
        subresult2 = str(sum(subresult))[-1]
        print("Sum of [" + " ".join(elements2sum) + "] = " + subresult2)
        result.append(subresult2)
        print("")
    return ''.join(result)

def run_phase(input, n):
    for i in range(n):
        print("### Phase", i)
        #print(i)
        input = phase(input)
    print(input)

input = "1111111"

run_phase(input, 4)

# input = input*2
#
# run_phase(input, 4)

#input = "80871224585914546619083218645595"

#run_phase(input, 4)
#
# input = "19617804207202209144916044189917"
#
# run_phase(input, 100)
#
# input = "69317163492948606335995924319873"
#
# run_phase(input, 100)

# with open('input.txt') as f:
#     input = f.read()
#
# #input = input*2
#
# run_phase(input, 100)

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))