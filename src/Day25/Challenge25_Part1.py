from math import prod
import networkx as nx

with open("/example/file/path.txt", 'r') as file:
    stream = file.read().splitlines()

data = {}
for line in stream:
    component, connections = line.split(":")
    data[component] = connections.strip().split()

G = nx.Graph()
for c, cc in data.items():
    for ci in cc:
        G.add_edge(c, ci)

cuts = nx.minimum_edge_cut(G)

G.remove_edges_from(cuts)

rg = list(nx.connected_components(G))

result = prod(len(i) for i in rg)
print(result)
