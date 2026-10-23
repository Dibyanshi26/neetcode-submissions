class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        # Ensure A is the shorter array
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        half = (m + n + 1) // 2

        low, high = 0, m

        while low <= high:
            i = (low + high) // 2
            j = half - i

            # Boundaries; use infinity to handle edge cuts
            A_left = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i] if i < m else float("inf")
            B_left = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j] if j < n else float("inf")

            # Check if partition is valid
            if A_left <= B_right and B_left <= A_right:
                if (m + n) % 2 == 1:
                    return float(max(A_left, B_left))
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            elif A_left > B_right:
                high = i - 1
            else:
                low = i + 1

        return 0.0