from collections import defaultdict


class Solution:
    # Time: O(k * n^2) where n = len(ring), k = len(key)
    # Space: O(n)
    def find_rotate_steps(self, ring: str, key: str) -> int:
        n = len(ring)
        positions: dict[str, list[int]] = defaultdict(list)
        for i, char in enumerate(ring):
            positions[char].append(i)

        dp = [0] * n
        for k in range(len(key) - 1, -1, -1):
            next_dp = [float("inf")] * n
            for i in range(n):
                for j in positions[key[k]]:
                    clockwise = abs(i - j)
                    steps = min(clockwise, n - clockwise)
                    next_dp[i] = min(next_dp[i], steps + 1 + dp[j])
            dp = next_dp
        return int(dp[0])
