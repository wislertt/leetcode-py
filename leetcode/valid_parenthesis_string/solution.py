class Solution:
    # Time: O(n)
    # Space: O(1)
    def check_valid_string(self, s: str) -> bool:
        # Range of possible open-parenthesis counts after processing each char.
        low = 0
        high = 0
        for char in s:
            if char == "(":
                low += 1
                high += 1
            elif char == ")":
                low = max(low - 1, 0)
                high -= 1
            else:  # '*' can act as '(', ')' or empty
                low = max(low - 1, 0)
                high += 1
            if high < 0:
                return False
        return low == 0
