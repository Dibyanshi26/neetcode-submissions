class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)           # turn nums into a min-heap
        while len(self.heap) > k:          # keep only the k largest
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)     # new number takes a seat
        if len(self.heap) > self.k:        # too many people?
            heapq.heappop(self.heap)       # kick out the smallest
        return self.heap[0]                # smallest of the top k = kth largest