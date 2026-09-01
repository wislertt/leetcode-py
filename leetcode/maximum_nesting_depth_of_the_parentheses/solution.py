class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_depth(self, s: str) -> int:
        depth = 0
        best = 0
        for char in s:
            if char == "(":
                depth += 1
                if depth > best:
                    best = depth
            elif char == ")":
                depth -= 1
        return best
