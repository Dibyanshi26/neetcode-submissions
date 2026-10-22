class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = []
        used = [False] * n

        def backtrack(current_path: list[int]):
            if len(current_path) == n:
                result.append(list(current_path))
                return

            for i in range(n):
                if used[i]:
                    continue

                used[i] = True
                current_path.append(nums[i])
                backtrack(current_path)
                current_path.pop()
                used[i] = False

        backtrack([])
        return result