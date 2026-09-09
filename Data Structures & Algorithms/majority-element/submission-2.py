class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            # Agar count 0 ho gaya, toh naya candidate chuno
            if count == 0:
                candidate = num

            # Agar candidate match hua toh +1, nahi toh -1
            if num == candidate:
                count += 1
            else:
                count -= 1

        # Aakhri mein jo candidate bacha wahi majority hai
        return candidate