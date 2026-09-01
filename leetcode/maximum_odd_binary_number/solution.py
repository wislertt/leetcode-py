class Solution:
    # Time: O(n)
    # Space: O(n)
    def maximum_odd_binary_number(self, s: str) -> str:
        ones = s.count("1")
        zeros = len(s) - ones
        return "1" * (ones - 1) + "0" * zeros + "1"
