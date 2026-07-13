class Solution:
    # Time: O(n^3) — n start indexes, n M values, up to 2M=2n X picks
    # Space: O(n^2) memo
    def stone_game_ii(self, piles: list[int]) -> int:
        n = len(piles)

        # suffix[i] = total stones in piles[i:]; lets the current player value
        # a move as suffix[i] - opponent_best_from_remaining.
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo: dict[tuple[int, int], int] = {}

        def best_from(i: int, m: int) -> int:
            # Max stones the player to move can collect from piles[i:] with bound M=m.
            if i >= n:
                return 0
            # Can take all remaining piles in one move.
            if i + 2 * m >= n:
                return suffix[i]
            if (i, m) in memo:
                return memo[(i, m)]

            best = 0
            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break
                taken = suffix[i] - suffix[i + x]
                opponent = best_from(i + x, max(m, x))
                best = max(best, taken + (suffix[i + x] - opponent))
            memo[(i, m)] = best
            return best

        return best_from(0, 1)
