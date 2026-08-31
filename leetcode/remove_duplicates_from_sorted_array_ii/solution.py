class Solution:
    # Time: O(n)
    # Space: O(1)
    def remove_duplicates(self, nums: list[int]) -> int:
        # Write index: next position for a kept value
        k = 0

        for num in nums:
            # Keep num if fewer than 2 kept copies exist so far.
            # nums[k - 2] != num means num appears at most once in the
            # kept prefix (nums[k - 2] is the earliest possible duplicate)
            if k < 2 or nums[k - 2] != num:
                nums[k] = num
                k += 1
        return k
