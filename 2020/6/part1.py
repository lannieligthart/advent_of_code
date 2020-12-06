with open('testinput.txt') as f:
    text = f.read().split("\n\n")

data = [t.replace("\n", "") for t in text]

questions = [len(set(d)) for d in data]

print(sum(questions))

