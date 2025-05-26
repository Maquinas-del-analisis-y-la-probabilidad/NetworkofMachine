# data stream management system
from main import packet_generator
from collections import deque
import ast

working_storage = [] # store the last 10 packets 
archival_storage = './res/archival.txt' 

def recive_packet(packet: dict): 
    with open(archival_storage, "a") as file: 
        file.write(f"{packet.__str__()}\n") # add all packets to archival storage

    if len(working_storage) <= 10:  
        working_storage.append(packet)
    else: 
        deque(working_storage)


# simulating the packet flow 
def flow_packets(): 
    while True: 
        current_packet = packet_generator()  
        recive_packet(current_packet) 


# Select * from packets.machienes when machine.status == $status
def get_machines_by_status(status: str): 
    with open(archival_storage, "r") as file: 
        lines = file.readlines()

    return [
        x
        for x in lines
        if ast.literal_eval(ast.literal_eval(x)["machine"])["status"] == status
    ]


if __name__ == "__main__": 
    machines = get_machines_by_status("Active")
    print(machines)
    #flow_packets()
