from collections import Counter


class Solution:
    # Time: O(n)
    # Space: O(n)
    def kth_distinct(self, arr: list[str], k: int) -> str:
        counts = Counter(arr)
        for s in arr:
            if counts[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""
