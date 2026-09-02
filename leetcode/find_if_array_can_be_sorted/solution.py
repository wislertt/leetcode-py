class Solution:
    # Time: O(n^2) worst case from sorting each segment
    # Space: O(n) for the working copy
    def can_sort_array(self, nums: list[int]) -> bool:
        arr = list(nums)
        n = len(arr)
        i = 0
        while i < n:
            bits = arr[i].bit_count()
            j = i
            while j < n and arr[j].bit_count() == bits:
                j += 1
            arr[i:j] = sorted(arr[i:j])
            i = j
        return arr == sorted(nums)
