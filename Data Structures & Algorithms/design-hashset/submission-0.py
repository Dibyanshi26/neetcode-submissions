class MyHashSet:

    def __init__(self):
        self.present = [False] * 1_000_001

    def add(self, key: int) -> None:
        self.present[key] = True

    def remove(self, key: int) -> None:
        self.present[key] = False

    def contains(self, key: int) -> bool:
        return self.present[key]