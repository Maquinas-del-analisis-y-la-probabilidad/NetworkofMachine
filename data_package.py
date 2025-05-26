import secrets


class DataPackage:
    def __init__(self, source_ip, destionation_ip, payload_size, flagged):
        self.source_ip = source_ip
        self.destionation_ip = destionation_ip
        self.payload_size = payload_size
        self.flagged = flagged


def data_package_generator() -> DataPackage:
    payload_size = secrets.randbelow(1401) + 100  # 100-1500
    flagged = secrets.choice([True, False])
    source_ip = ip_generator()
    destination_ip = ip_generator()
    return DataPackage(source_ip, destination_ip, payload_size, flagged)


def ip_generator() -> str:
    return ".".join([str(secrets.randbelow(256)) for _ in range(4)])
