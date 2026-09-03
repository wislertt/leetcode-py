class _MaxSegmentTree:
    """Segment tree supporting range chmax updates and range max queries."""

    def __init__(self, size: int) -> None:
        self.size = size
        self.tree = [0] * (4 * size)
        self.lazy = [0] * (4 * size)

    def _push_down(self, node: int) -> None:
        pending = self.lazy[node]
        if pending == 0:
            return
        for child in (2 * node, 2 * node + 1):
            if self.tree[child] < pending:
                self.tree[child] = pending
            if self.lazy[child] < pending:
                self.lazy[child] = pending
        self.lazy[node] = 0

    def update(self, left: int, right: int, value: int) -> None:
        self._update(1, 0, self.size - 1, left, right, value)

    def _update(self, node: int, start: int, end: int, left: int, right: int, value: int) -> None:
        if right < start or end < left:
            return
        if left <= start and end <= right:
            if self.tree[node] < value:
                self.tree[node] = value
            if self.lazy[node] < value:
                self.lazy[node] = value
            return
        self._push_down(node)
        mid = (start + end) // 2
        self._update(2 * node, start, mid, left, right, value)
        self._update(2 * node + 1, mid + 1, end, left, right, value)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, left: int, right: int) -> int:
        return self._query(1, 0, self.size - 1, left, right)

    def _query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        self._push_down(node)
        mid = (start + end) // 2
        return max(
            self._query(2 * node, start, mid, left, right),
            self._query(2 * node + 1, mid + 1, end, left, right),
        )


class Solution:
    # Time: O(n log n) with coordinate compression
    # Space: O(n)
    def falling_squares(self, positions: list[list[int]]) -> list[int]:
        coords: set[int] = set()
        for left, side in positions:
            coords.add(left)
            coords.add(left + side - 1)
        axis = sorted(coords)
        rank = {value: index for index, value in enumerate(axis)}
        tree = _MaxSegmentTree(len(axis))

        ans: list[int] = []
        tallest = 0
        for left, side in positions:
            lo = rank[left]
            hi = rank[left + side - 1]
            height = tree.query(lo, hi) + side
            tree.update(lo, hi, height)
            tallest = max(tallest, height)
            ans.append(tallest)
        return ans
