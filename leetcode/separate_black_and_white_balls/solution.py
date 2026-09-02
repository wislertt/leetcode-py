class Solution:
    # Time: O(n)
    # Space: O(1)
    def minimum_steps(self, s: str) -> int:
        steps = 0
        ones = 0
        for ball in s:
            if ball == "1":
                ones += 1
            else:
                steps += ones
        return steps
