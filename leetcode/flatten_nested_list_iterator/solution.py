from typing import Any


class NestedIterator:
    # Time: O(n) init + amortized O(1) per call  # n = total integers
    # Space: O(n)
    def __init__(self, nested_list: list[Any]) -> None:
        self._values: list[int] = []
        stack: list[Any] = list(reversed(nested_list))
        while stack:
            item = stack.pop()
            if isinstance(item, int):
                self._values.append(item)
            else:
                stack.extend(reversed(item))
        self._index = 0

    def next(self) -> int:
        value = self._values[self._index]
        self._index += 1
        return value

    def has_next(self) -> bool:
        return self._index < len(self._values)
