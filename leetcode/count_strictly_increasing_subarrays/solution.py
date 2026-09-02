class Solution:
    # Time: O(n)
    # Space: O(1)
    def count_strictly_increasing(self, nums: list[int]) -> int:
        total = 0
        run = 0
        prev = 0
        for i, x in enumerate(nums):
            if i > 0 and x > prev:
                run += 1
            else:
                run = 1
            total += run
            prev = x
        return total
