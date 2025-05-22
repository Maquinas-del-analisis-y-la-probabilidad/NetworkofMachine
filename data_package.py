import random


def ip_generator() -> str:
    return ".".join([random.randint(0, 255).__str__() for _ in range(4)])


class DataPackage:
    def __init__(self, source_ip, destionation_ip, payload_size, flagged):
        self.source_ip = source_ip
        self.destionation_ip = destionation_ip
        self.payload_size = payload_size
        self.flagged = flagged


def data_package_generator() -> DataPackage:
    payload_size = random.randint(100, 1500)
    flagged = random.choice([True, False])
    source_ip = ip_generator()
    destionation_ip = ip_generator()
    return DataPackage(source_ip, destionation_ip, payload_size, flagged)


if __name__ == "__main__":
    # sumulation of data strem of machines
    print(ip_generator())
