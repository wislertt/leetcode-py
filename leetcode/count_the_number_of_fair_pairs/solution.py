class Solution:
    # Time: O(n log n)
    # Space: O(n) for the sort
    def count_fair_pairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()

        def count_at_most(bound: int) -> int:
            left, right = 0, len(nums) - 1
            total = 0
            while left < right:
                if nums[left] + nums[right] <= bound:
                    total += right - left
                    left += 1
                else:
                    right -= 1
            return total

        return count_at_most(upper) - count_at_most(lower - 1)
