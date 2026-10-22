class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []

        def backtrack(start: int, remain: int, current_path: list[int]):
            if remain == 0:
                result.append(list(current_path))
                return

            for i in range(start, len(candidates)):
                # Early pruning: since array is sorted, subsequent numbers will also exceed remain
                if candidates[i] > remain:
                    break

                # Skip duplicate elements at the same tree depth/decision level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current_path.append(candidates[i])
                # Move to i + 1 because each candidate can be used at most once
                backtrack(i + 1, remain - candidates[i], current_path)
                current_path.pop()

        backtrack(0, target, [])
        return result