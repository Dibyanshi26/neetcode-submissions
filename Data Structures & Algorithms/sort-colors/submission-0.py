class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                # 0 ko low position par bhejo
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 already middle me hona chahiye
                mid += 1
            else:  # nums[mid] == 2
                # 2 ko high position par bhejo
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                # Notice: yahan mid += 1 nahi kiya kyunki high se jo number
                # swap hokar aaya hai, wo abhi uninspected (0, 1 ya 2) hai