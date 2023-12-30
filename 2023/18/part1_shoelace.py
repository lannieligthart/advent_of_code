
def shoelace(vertices):
    # A function to apply the Shoelace algorithm (calculate area of a polygon)
    # see https://www.101computing.net/the-shoelace-algorithm/
    numberOfVertices = len(vertices)
    sum1 = 0
    sum2 = 0

    for i in range(0, numberOfVertices - 1):
        sum1 = sum1 + vertices[i][0] * vertices[i + 1][1]
        sum2 = sum2 + vertices[i][1] * vertices[i + 1][0]

    # Add xn.y1
    sum1 = sum1 + vertices[numberOfVertices - 1][0] * vertices[0][1]
    # Add x1.yn
    sum2 = sum2 + vertices[0][0] * vertices[numberOfVertices - 1][1]

    area = abs(sum1 - sum2) / 2
    return area

with open("input.txt") as file:
    data = file.read().split("\n")

print(data)

r, c = (0, 0)
vertices = [(r, c)]
previous_drc = None

for d in data:
    d = d.split()
    drc, dist, col = d
    dist = int(dist)
    print(f"{drc}, {dist}; previous direction: {previous_drc}")
    if drc == "R":
        c += dist
        # right after down: add one to the column
        if previous_drc == "D":
            vertices[-1][1] += 1
    elif drc == "L":
        c -= dist
        # left after up: add one to the row
        if previous_drc == "U":
            vertices[-1][0] += 1
        elif previous_drc == "D":
            vertices[-1][1] += 1
            vertices[-1][0] += 1
    elif drc == "U":
        r -= dist
        # up after left: add one to the row
        if previous_drc == "L":
            vertices[-1][0] += 1
    elif drc == "D":
        r += dist
        # down after right: add one to the column
        if previous_drc == "R":
            vertices[-1][1] += 1
        if previous_drc == "L":
            vertices[-1][1] += 1
            vertices[-1][0] += 1
    previous_drc = drc
    vertices.append([r, c])





print(shoelace(vertices))







