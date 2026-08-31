class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_chunks_to_sorted(self, arr: list[int]) -> int:
        chunks = 0
        mx = 0
        for i, v in enumerate(arr):
            mx = max(mx, v)
            if mx == i:
                chunks += 1
        return chunks
