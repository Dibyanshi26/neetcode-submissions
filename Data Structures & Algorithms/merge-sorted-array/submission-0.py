class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        # Jab tak nums2 ke saare numbers nums1 me shift nahi ho jaate
        while p2 >= 0:
            # Agar nums1 ka element bada hai, usko end me place karo
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                # Warna nums2 ka element place karo
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1