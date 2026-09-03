class Solution:
    # Time: O(n)
    # Space: O(1)
    def num_subarray_bounded_max(self, nums: list[int], left: int, right: int) -> int:
        def at_most(bound: int) -> int:
            total = 0
            run = 0
            for value in nums:
                run = run + 1 if value <= bound else 0
                total += run
            return total

        return at_most(right) - at_most(left - 1)
