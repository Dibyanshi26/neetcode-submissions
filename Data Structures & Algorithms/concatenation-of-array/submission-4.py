class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        # 2n size ka list pehle se allocate kar liya
        ans = [0] * (2 * n)

        for i in range(n):
            ans[i] = nums[i]        # Pehla half
            ans[i + n] = nums[i]    # Doosra half

        return ans