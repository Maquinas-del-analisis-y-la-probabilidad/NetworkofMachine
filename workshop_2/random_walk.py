from data_packet import generate_data_packet
import networkx as nx
from networkx import DiGraph
import random

# genrate fake data
data = [generate_data_packet() for _ in range(10000)]


# build graph
graph = nx.DiGraph()

for packet in data:
    src = packet["dataPacket"]["sourceIP"]
    dst = packet["dataPacket"]["destinationIP"]
    graph.add_edge(src, dst)


# simulate el random walk
def random_walk(start_node, graph: DiGraph, steps):
    path = [start_node]
    current_node = start_node
    for _ in range(steps):
        neighbors = list(graph.successors(current_node))
        if not neighbors:
            break
        next = random.choice(neighbors)
        path.append(next)
        current_node = next

    return path


start = random.choice(list(graph.nodes))
walk = random_walk(start_node=start, graph=graph, steps=10)
print(f"El random walk es: {walk}")
