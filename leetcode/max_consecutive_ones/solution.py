class Solution:
    # Time: O(n)
    # Space: O(1)
    def find_max_consecutive_ones(self, nums: list[int]) -> int:
        best = 0
        current = 0
        for num in nums:
            if num == 1:
                current += 1
                best = max(best, current)
            else:
                current = 0
        return best
