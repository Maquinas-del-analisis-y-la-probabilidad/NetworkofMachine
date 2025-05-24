# Detecting malicious packages
# with hashing using reputation-based filtering

import hashlib
from data_package import data_package_generator
import time

black_list = [data_package_generator().__hash__() for _ in range(50)]


def main():
    print("black_list\n")
    for i in black_list:
        print(i)

    while True:
        package = data_package_generator()
        is_malicious_package = is_malicious(package)

        if is_malicious_package:
            print("Malicious package detected")
            print(package.__dict__)
            print(
                "Malicious package hash: ",
                package.__hash__(),
            )
            print("\n\n")

        time.sleep(0.5)


def is_malicious(package):
    package_hash = package.__hash__()
    return package_hash in black_list


if __name__ == "__main__":
    main()
