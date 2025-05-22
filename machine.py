import random
import uuid


class Machine:
    def __init__(self, id, type, status):
        self.id = id
        self.type = type
        self.status = status


status = ["Active", "Inactive", "Maintenance"]
types = ["Server", "Router", "Switch"]


def machine_generator():
    status_index = random.randint(0, len(status) - 1)
    type_index = random.randint(0, len(types) - 1)
    machine_id = uuid.uuid1()

    return Machine(
        id=machine_id.__str__(), type=types[type_index], status=status[status_index]
    )
