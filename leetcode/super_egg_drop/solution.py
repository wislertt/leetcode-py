class Solution:
    # Time: O(k * moves) where moves is the answer (moves <= n)
    # Space: O(k)
    def super_egg_drop(self, k: int, n: int) -> int:
        # coverage[i] = number of floors distinguishable with i eggs in the
        # current number of moves: coverage[i] = coverage[i] + coverage[i-1] + 1
        coverage = [0] * (k + 1)
        moves = 0
        while coverage[k] < n:
            moves += 1
            for eggs in range(k, 0, -1):
                coverage[eggs] += coverage[eggs - 1] + 1
        return moves
