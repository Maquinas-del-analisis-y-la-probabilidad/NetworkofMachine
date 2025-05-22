from machine import machine_generator
from data_package import data_package_generator
import time


def main():
    # sumulation of data strem of machines
    while True:
        machine = machine_generator()
        package = data_package_generator()
        time.sleep(0.25)
        dict = {machine: machine.__dict__, package: package.__dict__}
        print(dict)


if __name__ == "__main__":
    main()
