class Solution:
    # Time: O(n * max_jump)
    # Space: O(n)
    def cheapest_jump(self, coins: list[int], max_jump: int) -> list[int]:
        if coins[-1] == -1:
            return []
        n = len(coins)
        f = [float("inf")] * n
        f[-1] = coins[-1]
        for i in range(n - 2, -1, -1):
            if coins[i] != -1:
                for j in range(i + 1, min(n, i + max_jump + 1)):
                    if f[i] > f[j] + coins[i]:
                        f[i] = f[j] + coins[i]
        if f[0] == float("inf"):
            return []
        ans = []
        s = f[0]
        for i in range(n):
            if f[i] == s:
                s -= coins[i]
                ans.append(i + 1)
        return ans
