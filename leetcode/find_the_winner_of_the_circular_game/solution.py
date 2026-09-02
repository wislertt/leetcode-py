class Solution:
    # Time: O(n)
    # Space: O(1)
    def find_the_winner(self, n: int, k: int) -> int:
        # Josephus recurrence on 0-indexed survivors:
        # with `size` friends left, the survivor sits (k % size) positions
        # clockwise after the survivor of the `size - 1` round.
        winner = 0
        for size in range(2, n + 1):
            winner = (winner + k) % size
        return winner + 1
