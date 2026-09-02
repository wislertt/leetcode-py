class Solution:
    # Time: O(n * b) where b is the number of bits (32)
    # Space: O(1)
    def total_hamming_distance(self, nums: list[int]) -> int:
        total = 0
        for bit in range(32):
            ones = sum((num >> bit) & 1 for num in nums)
            total += ones * (len(nums) - ones)
        return total
