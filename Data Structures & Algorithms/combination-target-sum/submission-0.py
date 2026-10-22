class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []

        def backtrack(start: int, remain: int, current_path: list[int]):
            if remain == 0:
                result.append(list(current_path))
                return

            for i in range(start, len(nums)):
                if nums[i] > remain:
                    break

                current_path.append(nums[i])
                backtrack(i, remain - nums[i], current_path)
                current_path.pop()

        backtrack(0, target, [])
        return result