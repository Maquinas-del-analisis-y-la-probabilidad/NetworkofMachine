from collections import defaultdict
from data_packet import generate_data_packet

# generate data
data = [generate_data_packet() for _ in range(10000)]


# map ips related with danger pakages
def map_function(packet):
    if (
        packet["dataPacket"]["flagged"]
        and packet["dataPacket"]["threatLevel"] == "high"
    ):
        yield (packet["dataPacket"]["sourceIP"], 1)
        yield (packet["dataPacket"]["destinationIP"], 1)


intermediate = []
for packet in data:
    intermediate.extend(map_function(packet))

# group by id
grouped = defaultdict(list)
for ip, count in intermediate:
    grouped[ip].append(count)


# reduce: count ocurrencies by IP
def reduce_function(ip, counts):
    return (ip, sum(counts))


results = []
for ip, counts in grouped.items():
    results.append(reduce_function(ip, counts))

# Sort by most frequent IP
results.sort(key=lambda x: x[1], reverse=True)

print("The 10 most dangerous IPs")
for ip, count in results[:10]:
    print(f"{ip.__str__()}, {count}")
