class Solution:
    # Time: O(n)
    # Space: O(n)
    def max_chunks_to_sorted(self, arr: list[int]) -> int:
        n = len(arr)
        prefix_max = [0] * n
        prefix_max[0] = arr[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], arr[i])

        suffix_min = [0] * n
        suffix_min[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], arr[i])

        chunks = 1
        for i in range(n - 1):
            if prefix_max[i] <= suffix_min[i + 1]:
                chunks += 1
        return chunks
