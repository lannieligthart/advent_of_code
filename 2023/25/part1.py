from dash import Dash, html
import dash_cytoscape as cyto

with open("input.txt") as file:
    data = file.read().split("\n")

def remove_conn(diagram, combo):
    c1, c2 = combo
    diagram[c1].remove(c2)
    diagram[c2].remove(c1)
    return diagram


diagram = dict()

for d in data:
    name, connections = d.split(": ")
    connections = connections.split()
    diagram[name] = []
    for c in connections:
        diagram[c] = []

# add connections
for d in data:
    name, connections = d.split(": ")
    connections = connections.split()
    for c in connections:
        diagram[name].append(c)
        diagram[c].append(name)


# combos = set()
# for key, value in diagram.items():
#     for v in value:
#         combos.add((key, v))
# elements = []
# for c in combos:
#     elements.append({'data': {'source': c[0], 'target': c[1]}})
# for key in diagram.keys():
#     elements.append({'data': {'id': key, 'label': key}})
#
#
# app = Dash(__name__)
#
# app.layout = html.Div([
#     html.P("Dash Cytoscape:"),
#     cyto.Cytoscape(
#         id='cytoscape',
#         elements=elements,
#         layout={'name': 'breadthfirst'},
#         style={'width': '1000px', 'height': '1000px'}
#     )
# ])
#
# app.run_server(debug=True)


# after visual inspection of the graph, these seem to be the one that need to be disconnected.
diagram = remove_conn(diagram, ("kns", "dct"))
diagram = remove_conn(diagram, ("nqq", "pxp"))
diagram = remove_conn(diagram, ("jxb", "ksq"))

# count the ones in the first group
counted = []
nodes = ['hhh']
while True:
    newnodes = []
    for n in nodes:
        conn = diagram[n]
        for c in conn:
            if c not in counted:
                counted.append(c)
                newnodes.append(c)
    if len(newnodes) == 0:
        break
    nodes = newnodes

assert len(counted) * (len(diagram.keys()) - len(counted)) == 583338




