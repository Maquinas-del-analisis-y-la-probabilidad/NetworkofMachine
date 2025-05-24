# Storing machines profiles in a dictionary

import random
import uuid

machines = {}


# this function generates a ramdom machine profile
def machine_profile_generator() -> dict:
    return {
        "id": uuid.uuid4().hex,
        "type": random.choice(["server", "router", "switch"]),
        "status": random.choice(["active", "inactive", "maintenance"]),
        "prcessing_captability": random.randint(1, 100),  # in percentage
    }


# simulating a data_stream of machine profiles
def data_stream_generator():
    for _ in range(10):
        current_machine = machine_profile_generator()
        machines[current_machine["id"]] = current_machine


def main():
    data_stream_generator()
    print("Machines profiles saved in the dictionary:\n")
    print(machines)


if __name__ == "__main__":
    main()
