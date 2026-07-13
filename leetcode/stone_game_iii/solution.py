class Solution:
    # Time: O(n)
    # Space: O(n)
    def stone_game_iii(self, stone_value: list[int]) -> str:
        n = len(stone_value)

        # dp[i] = best score advantage the player to move can build over the
        # opponent from stone_value[i:] (positive => current player leads).
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            best = -(10**18)
            taken = 0
            for x in range(i, min(i + 3, n)):
                taken += stone_value[x]
                # Current pockets `taken`, then opponent enjoys dp[x + 1].
                best = max(best, taken - dp[x + 1])
            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"
