from bisect import bisect_left, bisect_right


class RangeModule:
    # Time: add/remove O(n) per call, query O(log n)
    # Space: O(n) for the tracked disjoint intervals
    def __init__(self) -> None:
        # Parallel sorted arrays describing disjoint, non-adjacent half-open
        # intervals: the i-th tracked range is [starts[i], ends[i]).
        self.starts: list[int] = []
        self.ends: list[int] = []

    # Time: O(n)
    # Space: O(n)
    def add_range(self, left: int, right: int) -> None:
        # First interval whose end reaches left, and first interval that
        # starts at or after right: every interval in between overlaps and
        # must be absorbed into the merged range.
        i = bisect_left(self.ends, left)
        j = bisect_left(self.starts, right)
        if i < j:
            left = min(left, self.starts[i])
            right = max(right, self.ends[j - 1])
        self.starts[i:j] = [left]
        self.ends[i:j] = [right]

    # Time: O(log n)
    # Space: O(1)
    def query_range(self, left: int, right: int) -> bool:
        i = bisect_right(self.starts, left) - 1
        return i >= 0 and self.ends[i] >= right

    # Time: O(n)
    # Space: O(n)
    def remove_range(self, left: int, right: int) -> None:
        i = bisect_left(self.ends, left)
        j = bisect_left(self.starts, right)
        if i >= j:
            return
        kept: list[tuple[int, int]] = []
        if self.starts[i] < left:
            kept.append((self.starts[i], left))
        if self.ends[j - 1] > right:
            kept.append((right, self.ends[j - 1]))
        self.starts[i:j] = [start for start, _ in kept]
        self.ends[i:j] = [end for _, end in kept]
