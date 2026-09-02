class Solution:
    # Time: O(n)
    # Space: O(n)
    def h_index(self, citations: list[int]) -> int:
        n = len(citations)
        buckets = [0] * (n + 1)
        for c in citations:
            buckets[min(c, n)] += 1
        total = 0
        for h in range(n, -1, -1):
            total += buckets[h]
            if total >= h:
                return h
        return 0
