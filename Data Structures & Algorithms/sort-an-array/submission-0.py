class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge_sort(arr: list[int], left: int, right: int) -> None:
            # Base Case: Single element ya invalid range already sorted hoti hai
            if left >= right:
                return

            mid = (left + right) // 2

            # Left aur Right halves ko recursively sort karo
            merge_sort(arr, left, mid)
            merge_sort(arr, mid + 1, right)

            # Sorted halves ko merge karo
            merge(arr, left, mid, right)

        def merge(arr: list[int], left: int, mid: int, right: int) -> None:
            # Dono sorted halves ki temporary copies banao
            L = arr[left:mid + 1]
            R = arr[mid + 1:right + 1]

            i = 0  # Pointer for L
            j = 0  # Pointer for R
            k = left  # Original array par overwrite karne ke liye pointer

            # Chhote element ko original array me place karo
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # Agar L me koi elements bach gaye hon
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            # Agar R me koi elements bach gaye hon
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

        merge_sort(nums, 0, len(nums) - 1)
        return nums