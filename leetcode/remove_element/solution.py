class Solution:
    # Time: O(n)
    # Space: O(1)
    def remove_element(self, nums: list[int], val: int) -> int:
        write = 0
        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        return write
