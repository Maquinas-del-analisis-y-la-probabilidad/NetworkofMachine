from DGIM import DGIMAlgorithm
from data_package import DataPackage, data_package_generator

streams = [data_package_generator() for _ in range(1000)]


def main():
    dgim = DGIMAlgorithm(N=1000)
    for stream in streams:
        if stream.flagged:
            dgim.update(1)
        else:
            dgim.update(0)

    print("El numero de paquetes maliciosos en los ultimos 1000 es de:")
    print(dgim.estimate())


if __name__ == "__main__":
    main()
