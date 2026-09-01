class Solution:
    # Time: O(n) single pass over the diagonal
    # Space: O(n) for the result string
    def find_unique_binary_string(self, nums: list[str]) -> str:
        # Cantor diagonal: flipping nums[i][i] differs from nums[i] at position i,
        # so the result differs from every string in nums.
        return "".join("1" if s[i] == "0" else "0" for i, s in enumerate(nums))
