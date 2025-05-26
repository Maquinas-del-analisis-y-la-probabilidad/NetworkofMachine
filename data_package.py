import secrets


class DataPackage:
    def __init__(
        self, source_ip: str, destionation_ip: str, payload_size: int, flagged: bool
    ):
        self.source_ip: str = source_ip
        self.destionation_ip: str = destionation_ip
        self.payload_size: int = payload_size
        self.flagged: bool = flagged

    def get_hash(self, size: int = 10000000) -> int:
        hash_count: int = 0
        for i, char in enumerate(self._get_str()):
            hash_count += ord(char) * i
        return hash_count % size

    def _get_str(self) -> str:
        return (
            self.destionation_ip
            + self.source_ip
            + self.payload_size.__str__()
            + self.flagged.__str__()
        )


def data_package_generator() -> DataPackage:
    payload_size = secrets.randbelow(1401) + 100  # 100-1500
    flagged = secrets.choice([True, False])
    source_ip = ip_generator()
    destination_ip = ip_generator()
    return DataPackage(source_ip, destination_ip, payload_size, flagged)


def ip_generator() -> str:
    return ".".join([str(secrets.randbelow(256)) for _ in range(4)])


if __name__ == "__main__":
    print(data_package_generator().get_hash())
