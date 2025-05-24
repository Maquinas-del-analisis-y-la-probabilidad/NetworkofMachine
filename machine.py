import random
import uuid
import data_package


class Machine:
    def __init__(self, id, type, status):
        self.id = id
        self.type = type
        self.status = status
        self.ip_direction = data_package.ip_generator()


status = ["Active", "Inactive", "Maintenance"]
types = ["Server", "Router", "Switch"]


def machine_generator():
    status_machine = random.choice(status)
    type_machine = random.choice(types)
    machine_id = uuid.uuid1().__str__()

    return Machine(id=machine_id, type=type_machine, status=status_machine)
