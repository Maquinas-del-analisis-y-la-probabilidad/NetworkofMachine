import networkx as nx
from data_packet import generate_data_packet

data = [generate_data_packet() for _ in range(10000)]

graph = nx.DiGraph()

for entry in data:
    src = entry["dataPacket"]["sourceIP"]
    dst = entry["dataPacket"]["destinationIP"]
    graph.add_edge(src, dst)

pagerank = nx.pagerank(graph)

top_critical_nodes = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:10]
for ip, score in top_critical_nodes:
    print(f"IP: {ip}, PageRank Score: {score:.5f}")

