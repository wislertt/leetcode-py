class Solution:
    # Time: O(n^4) with n <= 10: n-1 split points, each side yields at most 2 valid forms
    # Space: O(n^2) output, all coordinate strings
    def ambiguous_coordinates(self, s: str) -> list[str]:
        def forms(digits: str) -> list[str]:
            out: list[str] = []
            for i in range(1, len(digits) + 1):
                head, tail = digits[:i], digits[i:]
                if head != "0" and head.startswith("0"):
                    continue
                if tail.endswith("0"):
                    continue
                out.append(head + "." + tail if tail else head)
            return out

        results: list[str] = []
        digits = s[1:-1]
        for i in range(1, len(digits)):
            for left in forms(digits[:i]):
                for right in forms(digits[i:]):
                    results.append("(" + left + ", " + right + ")")
        return results
