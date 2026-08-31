from collections import Counter


class Solution:
    # Time: O(len(text))
    # Space: O(1)
    def max_number_of_balloons(self, text: str) -> int:
        counts = Counter(text)
        return min(counts["b"], counts["a"], counts["l"] // 2, counts["o"] // 2, counts["n"])
