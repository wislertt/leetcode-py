class Solution:
    # Time: O(n)
    # Space: O(1)
    def min_operations(self, nums: list[int]) -> int:
        arr = list(nums)
        ops = 0
        for i in range(len(arr) - 2):
            if arr[i] == 0:
                ops += 1
                arr[i] = 1
                arr[i + 1] ^= 1
                arr[i + 2] ^= 1
        if 0 in arr:
            return -1
        return ops
