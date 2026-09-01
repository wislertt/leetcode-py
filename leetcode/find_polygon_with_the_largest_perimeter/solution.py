class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def largest_perimeter(self, nums: list[int]) -> int:
        sides = sorted(nums)
        total = sum(sides)
        for i in range(len(sides) - 1, 1, -1):
            if total - sides[i] > sides[i]:
                return total
            total -= sides[i]
        return -1
