class Solution:
    # Time: O(n)
    # Space: O(1)
    def find_min_moves(self, machines: list[int]) -> int:
        n = len(machines)
        total = sum(machines)
        if total % n != 0:
            return -1
        target = total // n
        moves = 0
        balance = 0
        for count in machines:
            diff = count - target
            balance += diff
            moves = max(moves, abs(balance), diff)
        return moves
