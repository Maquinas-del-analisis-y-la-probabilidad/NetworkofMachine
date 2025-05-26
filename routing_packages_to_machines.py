import data_package
from machine import machine_generator
from data_package import data_package_generator
import random
import time

machines = [machine_generator() for _ in range(4)]
machine_ips = [machine.ip_direction for machine in machines]


def main():
    print("\n machines \n")
    for machine in machines:
        print(machine.__dict__)

    print("\n data packages \n")
    while True:
        package = data_package_generator()
        package.destionation_ip = random.choice(machine_ips)
        print(package.__dict__)
        print(hash(package))
        time.sleep(0.25)


if __name__ == "__main__":
    main()
