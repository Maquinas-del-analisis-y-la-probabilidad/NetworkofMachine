from pybloom_live import BloomFilter 
import ast 

malware_packets = BloomFilter(capacity=10000000, error_rate=0.01)


# cargar todos los paquetes que son conocidos como maliciosos
def retrive_malware_packets(): 
    with open("./res/malware_packets.txt", "r") as file: 
        lines = file.readlines()
    
    for line in lines: 
        malware_packets.add(ast.literal_eval(line))
    

def is_malicious_packet(packet):
    return packet in malware_packets



def main(): 
    malware = {'_id': 'e07db975-39ba-11f0-ada7-2c3b70e344c4', 'machine': "{'id': 'e07dc78f-39ba-11f0-8de0-2c3b70e344c4', 'type': 'Router', 'status': 'Maintenance', 'ip_direction': '201.236.35.96'}", 'package': "{'source_ip': '78.133.128.238', 'destionation_ip': '158.220.59.110', 'payload_size': 970, 'flagged': True}", 'time_stamp': '2025-05-25T17:52:04.152580'}
        
    print(f"malware packet: \n{malware}")

    print("testing bloom filter")
    print(is_malicious_packet(malware))


if __name__ == "__main__": 
    retrive_malware_packets()
    main()
