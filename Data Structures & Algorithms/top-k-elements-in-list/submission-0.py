from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Har number ka count nikalo
        count = Counter(nums)

        # Step 2: Buckets initialize karo (0 se len(nums) tak)
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3: Har number ko uski frequency wale index ke bucket me daalo
        for num, freq in count.items():
            buckets[freq].append(num)

        # Step 4: Highest frequency (right) se collect karna shuru karo
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result