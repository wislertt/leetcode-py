class Excel:
    # Time: get/sum O(reachable formula graph) per call
    # Space: O(height * width)
    def __init__(self, height: int, width: str) -> None:
        self.height = height
        self.width = ord(width) - 64
        self.contents: dict[tuple[int, int], int | list[str]] = {}

    def set(self, row: int, column: str, val: int) -> None:
        self.contents[(row, ord(column) - 64)] = val

    def get(self, row: int, column: str) -> int:
        return self._value(row, ord(column) - 64)

    def sum(self, row: int, column: str, numbers: list[str]) -> int:
        self.contents[(row, ord(column) - 64)] = numbers
        return self._value(row, ord(column) - 64)

    def _value(self, row: int, col: int) -> int:
        content = self.contents.get((row, col))
        if content is None:
            return 0
        if isinstance(content, int):
            return content
        return sum(self._parse(token) for token in content)

    def _parse(self, token: str) -> int:
        if ":" not in token:
            return self._value(int(token[1:]), ord(token[0]) - 64)
        top_left, bottom_right = token.split(":")
        r1, r2 = int(top_left[1:]), int(bottom_right[1:])
        c1, c2 = ord(top_left[0]) - 64, ord(bottom_right[0]) - 64
        return sum(self._value(r, c) for r in range(r1, r2 + 1) for c in range(c1, c2 + 1))
