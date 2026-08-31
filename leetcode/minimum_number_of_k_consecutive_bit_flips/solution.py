class Solution:
    # Time: O(n)
    # Space: O(n)
    def min_k_bit_flips(self, nums: list[int], k: int) -> int:
        n = len(nums)
        flip_ends: list[bool] = [False] * n
        flipped = 0
        flips = 0
        for i, num in enumerate(nums):
            if i >= k and flip_ends[i - k]:
                flipped ^= 1
            if (num ^ flipped) == 0:
                if i + k > n:
                    return -1
                flipped ^= 1
                flip_ends[i] = True
                flips += 1
        return flips
