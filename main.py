from machine import machine_generator
from data_package import data_package_generator
import datetime
import uuid


def main():
    print("Hello world")


def packet_generator():
    return {
        "_id": uuid.uuid1().__str__(),
        "machine": machine_generator().__dict__.__str__(),
        "package": data_package_generator().__dict__.__str__(),
        "time_stamp": datetime.datetime.now().isoformat().__str__(),
    }


if __name__ == "__main__":
    main()
