from collections import deque


class DGIMBucket:
    def __init__(self, timestamp, count):
        self.timestamp = timestamp  # Timestamp of the bucket's end
        self.count = count  # Count of "1"s in the bucket

    def __repr__(self):
        return f"DGIMBucket(timestamp={self.timestamp}, count={self.count})"


class DGIMAlgorithm:
    def __init__(self, N):
        self.N = N  # Size of the window of interest
        self.buckets = deque()  # Buckets for counting "1"s
        self.next_timestamp = 0  # Timestamp of the next bit

    def update(self, bit):
        # print(f"Updating with bit: {bit}")

        # If the bit is "1", create a new bucket
        if bit == 1:
            new_bucket = DGIMBucket(self.next_timestamp, 1)
            self.buckets.appendleft(new_bucket)
            # print(f"Added new bucket: {new_bucket}")

        # Remove buckets that are older than N
        while (
            self.buckets and self.buckets[-1].timestamp <= self.next_timestamp - self.N
        ):
            old_bucket = self.buckets.pop()
            # print(f"Removing old bucket: {old_bucket}")

        # Merge buckets if there are more than 2 buckets with the same count
        # Start from the oldest buckets and move towards the newest
        i = len(self.buckets) - 1
        while i > 1:
            if (
                self.buckets[i].count
                == self.buckets[i - 1].count
                == self.buckets[i - 2].count
            ):
                merged_bucket = self.buckets[i - 1]
                merged_bucket.count += self.buckets[i].count
                # print(f"Merging buckets: {merged_bucket} and {self.buckets[i]}")
                del self.buckets[i]  # Correct way to remove an element by index
                i -= 1  # After merging, move the index back to check again
            i -= 1

        self.next_timestamp += 1
        # print(f"Buckets after update: {list(self.buckets)}")

    def estimate(self):
        # Estimate the count of "1"s in the last N bits
        estimate = 0
        if self.buckets:
            # Sum the counts of all buckets except the last one
            for bucket in list(self.buckets)[:-1]:
                estimate += bucket.count
            # Add half of the count of the last bucket to avoid overcounting
            estimate += self.buckets[-1].count // 2
        print(f"Estimated number of '1's: {estimate}")
        return estimate
