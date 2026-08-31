from bisect import bisect_left


class SummaryRanges:
    # Maintains starts sorted; interval i covers [starts[i], ends[i]].
    # add_num: O(log n) lookup + O(n) list insert; get_intervals: O(k).
    # Space: O(n)
    def __init__(self) -> None:
        self._starts: list[int] = []
        self._ends: list[int] = []

    def add_num(self, value: int) -> None:
        index = bisect_left(self._starts, value)
        if index < len(self._starts) and self._starts[index] == value:
            return  # duplicate
        # value lands strictly between interval index-1 and index
        left_adjacent = index > 0 and self._ends[index - 1] == value - 1
        right_adjacent = index < len(self._starts) and self._starts[index] == value + 1
        if left_adjacent and right_adjacent:
            # bridge the two intervals
            self._ends[index - 1] = self._ends[index]
            del self._starts[index]
            del self._ends[index]
        elif left_adjacent:
            self._ends[index - 1] = value
        elif right_adjacent:
            self._starts[index] = value
        else:
            self._starts.insert(index, value)
            self._ends.insert(index, value)

    def get_intervals(self) -> list[list[int]]:
        return [[start, end] for start, end in zip(self._starts, self._ends, strict=True)]
