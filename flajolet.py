from data_package import data_package_generator, DataPackage

stream = [data_package_generator() for _ in range(10000)]


def trailing_zeros(x: int):
    return len(bin(x)) - len(bin(x).rstrip("0"))


def flajolet_martin(stream: list[DataPackage]) -> int:
    max_zero = 0
    for packet in stream:
        h = packet.get_hash()
        tz = trailing_zeros(h)
        max_zero = max(max_zero, tz)
    return 2**max_zero


def main():
    print("Elementos diferentes en el stream")
    print(flajolet_martin(stream))


if __name__ == "__main__":
    main()
