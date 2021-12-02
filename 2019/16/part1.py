import time

startTime = time.time()

input = "12345678"

repeat_seq = [0, 1, 0, -1]

output = []
def get_repseq(n, repeat_seq):
    # deze kunnen we op een efficiëntere manier bepalen. 
    result = [x for x in repeat_seq for i in range(n)]
    # repeat this sequence the number of times required to reach length len + 1
    return result

def phase(input):
    result = []
    for n in range(1, len(input) + 1):
        subresult = []
        repseq = get_repseq(n, repeat_seq)
        for i in range(len(str(input))):
            element = int(str(input)[i])
            rs_i = (i % len(repseq) + 1)
            if rs_i == len(repseq):
                rs_i = 0
            #print(str(element), str(repseq[rs_i]))
            tmp = element * repseq[rs_i]
            subresult.append(tmp)
        subresult = str(sum(subresult))[-1]
        result.append(subresult)
    return ''.join(result)

def run_phase(input, n):
    for i in range(n):
        #print(i)
        input = phase(input)
    print(input)

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

with open('input.txt') as f:
    input = f.read()

run_phase(input, 100)

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))