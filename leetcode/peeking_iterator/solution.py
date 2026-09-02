class Iterator:
    def __init__(self, nums: list[int]) -> None:
        self._nums: list[int] = list(nums)
        self._index: int = 0

    def next(self) -> int:
        value = self._nums[self._index]
        self._index += 1
        return value

    def has_next(self) -> bool:
        return self._index < len(self._nums)


class PeekingIterator(Iterator):
    # Time: O(1) per call
    # Space: O(1)
    def __init__(self, iterator: Iterator) -> None:
        self._iterator = iterator
        self._peeked = 0
        self._has_peeked = False

    def peek(self) -> int:
        if not self._has_peeked:
            self._peeked = self._iterator.next()
            self._has_peeked = True
        return self._peeked

    def next(self) -> int:
        if self._has_peeked:
            self._has_peeked = False
            return self._peeked
        return self._iterator.next()

    def has_next(self) -> bool:
        return self._has_peeked or self._iterator.has_next()
