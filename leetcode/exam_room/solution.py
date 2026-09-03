import heapq
from bisect import bisect_left, insort


class ExamRoom:
    # Time: __init__ O(1), seat O(log k) amortized, leave O(log k + k)
    # Space: O(k) for k occupied seats

    def __init__(self, n: int) -> None:
        self.n = n
        self.occupied: list[int] = []
        self.gaps: list[tuple[int, int, int]] = []
        self._push(-1, n)

    def _push(self, left: int, right: int) -> None:
        if right - left < 2:
            return
        if left == -1:
            dist = right
        elif right == self.n:
            dist = self.n - 1 - left
        else:
            dist = (right - left) // 2
        heapq.heappush(self.gaps, (-dist, left, right))

    def _valid(self, left: int, right: int) -> bool:
        occ = self.occupied
        if left == -1:
            return (right == self.n) if not occ else occ[0] == right
        if right == self.n:
            return occ[-1] == left
        i = bisect_left(occ, left)
        return i + 1 < len(occ) and occ[i] == left and occ[i + 1] == right

    def seat(self) -> int:
        while True:
            _, left, right = heapq.heappop(self.gaps)
            if not self._valid(left, right):
                continue
            if left == -1:
                pos = 0
            elif right == self.n:
                pos = self.n - 1
            else:
                pos = (left + right) // 2
            insort(self.occupied, pos)
            self._push(left, pos)
            self._push(pos, right)
            return pos

    def leave(self, p: int) -> None:
        self.occupied.remove(p)
        i = bisect_left(self.occupied, p)
        left = self.occupied[i - 1] if i > 0 else -1
        right = self.occupied[i] if i < len(self.occupied) else self.n
        self._push(left, right)
