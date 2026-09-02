class Solution:
    # Time: O(n + k)
    # Space: O(1)
    def number_of_alternating_groups(self, colors: list[int], k: int) -> int:
        n = len(colors)
        count = 0
        run = 1
        for i in range(1, n + k - 1):
            run = run + 1 if colors[i % n] != colors[(i - 1) % n] else 1
            if run >= k:
                count += 1
        return count
