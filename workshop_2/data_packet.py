import random
import uuid
from faker import Faker
from datetime import datetime

fake = Faker()

ips = [fake.ipv4() for _ in range(50)]


def generate_data_packet():
    data = {
        "_id": str(uuid.uuid4().hex[:24]),  # simulando un objectId (24 hex chars)
        "machine": {
            "id": str(uuid.uuid4()),
            "type": random.choice(["server", "router", "switch"]),
            "status": random.choice(["online", "offline", "maintenance"]),
        },
        "dataPacket": {
            "sourceIP": random.choice(ips).__str__(),
            "destinationIP": random.choice(ips).__str__(),
            "payloadSize": random.randint(100, 1500),
            "flagged": random.choice([True, False]),
            "threatLevel": random.choice(["low", "medium", "high"]),
        },
        "timestamp": fake.date_time_between(start_date="-3y", end_date="now").strftime(
            "%Y-%m-%dT%H:%M:%S %z"
        ),
        "securityScore": random.randint(1, 100),
    }
    return data


# Ejemplo de uso
if __name__ == "__main__":
    json = generate_data_packet()
    print(json)
