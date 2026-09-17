class MyHashMap:
    def __init__(self):
        self.size = 1009  # use a prime number for better distribution
        self.buckets = [[] for _ in range(self.size)]
 
    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx][i] = (key, value)
                return
        self.buckets[idx].append((key, value))
 
    def get(self, key: int) -> int:
        idx = key % self.size
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return -1
 
    def remove(self, key: int) -> None:
        idx = key % self.size
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return