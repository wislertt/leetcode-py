class Vector2D:
    # Time: O(1) amortized per call
    # Space: O(1)
    def __init__(self, vec: list[list[int]]) -> None:
        self.vec = vec
        self.row = 0
        self.col = 0

    def _skip_empty_rows(self) -> None:
        while self.row < len(self.vec) and self.col == len(self.vec[self.row]):
            self.row += 1
            self.col = 0

    def next(self) -> int:
        self._skip_empty_rows()
        value = self.vec[self.row][self.col]
        self.col += 1
        return value

    def has_next(self) -> bool:
        self._skip_empty_rows()
        return self.row < len(self.vec)
