def _line_swaps(masks: list[int], n: int) -> int:
    """Min swaps to make one axis alternate, or -1 if that axis cannot."""
    full = (1 << n) - 1
    first = masks[0]
    if set(masks) != {first, full ^ first}:
        return -1
    ones = bin(first).count("1")
    if ones * 2 not in (n - 1, n, n + 1):
        return -1
    count_first = masks.count(first)
    if abs(count_first - (n - count_first)) > 1:
        return -1
    need_even = (n + 1) // 2
    best = -1
    for even_mask in (first, full ^ first):
        if masks.count(even_mask) != need_even:
            continue
        target = [even_mask if i % 2 == 0 else full ^ even_mask for i in range(n)]
        misplaced = sum(1 for i in range(n) if masks[i] != target[i])
        swaps = misplaced // 2
        best = swaps if best < 0 else min(best, swaps)
    return best


class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def moves_to_chessboard(self, board: list[list[int]]) -> int:
        n = len(board)
        rows = [sum(cell << j for j, cell in enumerate(row)) for row in board]
        cols = [sum(board[i][j] << i for i in range(n)) for j in range(n)]
        total = 0
        for masks in (rows, cols):
            swaps = _line_swaps(masks, n)
            if swaps < 0:
                return -1
            total += swaps
        return total
