class Solution:
    # Time: O(sqrt(target)) - the loop runs about sqrt(2 * |target|) times
    # Space: O(1)
    def reach_number(self, target: int) -> int:
        target = abs(target)
        moves = 0
        total = 0
        while total < target or (total - target) % 2:
            moves += 1
            total += moves
        return moves
