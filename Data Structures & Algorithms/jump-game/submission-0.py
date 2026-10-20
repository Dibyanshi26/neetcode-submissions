class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        last_index = len(nums) - 1

        for i, jump in enumerate(nums):
            # If current index is beyond the farthest reachable point, we are stuck
            if i > max_reach:
                return False

            max_reach = max(max_reach, i + jump)

            # Early exit: we can already reach or exceed the last index
            if max_reach >= last_index:
                return True

        return True