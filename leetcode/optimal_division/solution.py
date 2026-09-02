class Solution:
    # Time: O(n)
    # Space: O(n)
    def optimal_division(self, nums: list[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return f"{nums[0]}/{nums[1]}"
        return f"{nums[0]}/(" + "/".join(str(x) for x in nums[1:]) + ")"
