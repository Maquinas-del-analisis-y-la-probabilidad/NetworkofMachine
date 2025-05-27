import random
from data_package import data_package_generator
import time


def reservoir_sampling(size: int):
    sample = []
    counter = 0
    while True:
        current_packet = data_package_generator()
        if counter < size:
            sample.append(current_packet.__dict__.__str__())
        else:
            index = random.randint(0, counter)
            if index < size:
                sample[index] = current_packet.__dict__.__str__()

        counter += 1

        print("Sample: \n")
        print(sample)
        print("\n")
        time.sleep(0.5)


def main():
    reservoir_sampling(size=2)


if __name__ == "__main__":
    main()
