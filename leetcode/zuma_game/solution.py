_UNREACHABLE = 10**9


def _clean(row: str) -> str:
    while True:
        kept: list[str] = []
        i = 0
        while i < len(row):
            j = i
            while j < len(row) and row[j] == row[i]:
                j += 1
            if j - i < 3:
                kept.append(row[i:j])
            i = j
        nxt = "".join(kept)
        if nxt == row:
            return row
        row = nxt


def _adjacent(row: str, pos: int, ball: str) -> bool:
    return (pos > 0 and row[pos - 1] == ball) or (pos < len(row) and row[pos] == ball)


class Solution:
    # Time: O((n + h)^h * n * h) states over memoized rows, n <= 21, h <= 5
    # Space: O(states) memo plus recursion depth h
    def find_min_step(self, board: str, hand: str) -> int:
        memo: dict[tuple[str, str], int] = {}

        def search(row: str, balls: str) -> int:
            if not row:
                return 0
            if (row, balls) in memo:
                return memo[(row, balls)]
            if not balls:
                return _UNREACHABLE
            best = _UNREACHABLE
            for i, ball in enumerate(balls):
                if i > 0 and balls[i - 1] == ball:
                    continue
                rest = balls[:i] + balls[i + 1 :]
                for pos in range(len(row) + 1):
                    if not _adjacent(row, pos, ball):
                        continue
                    nxt = _clean(row[:pos] + ball + row[pos:])
                    best = min(best, 1 + search(nxt, rest))
            memo[(row, balls)] = best
            return best

        result = search(board, "".join(sorted(hand)))
        return -1 if result >= _UNREACHABLE else result
