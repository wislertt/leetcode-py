class Solution:
    # Time: O(n * 2^n)
    # Space: O(n * 2^n)
    def diff_ways_to_compute(self, expression: str) -> list[int]:
        results: list[int] = []
        for i, ch in enumerate(expression):
            if ch in "+-*":
                left = self.diff_ways_to_compute(expression[:i])
                right = self.diff_ways_to_compute(expression[i + 1 :])
                for left_val in left:
                    for right_val in right:
                        if ch == "+":
                            results.append(left_val + right_val)
                        elif ch == "-":
                            results.append(left_val - right_val)
                        else:
                            results.append(left_val * right_val)
        if not results:
            results.append(int(expression))
        return results
