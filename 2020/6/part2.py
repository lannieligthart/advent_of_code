with open('input.txt') as f:
    text = f.read().split("\n\n")

groups = [t.split("\n") for t in text]
questions_per_group = [set(t.replace("\n", "")) for t in text]

def count_n_in_all(group, questions):
    count = 0
    for q in questions:
        n = 0
        for person in group:
            if q in person:
                n += 1
        if n == len(group):
            count += 1
    return count

total_questions = 0
for i in range(len(groups)):
    total_questions += count_n_in_all(groups[i], questions_per_group[i])
print(total_questions)

assert total_questions == 3640