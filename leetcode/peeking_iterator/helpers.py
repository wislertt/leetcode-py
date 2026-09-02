class Iterator:
    def __init__(self, nums: list[int]) -> None:
        self.nums: list[int] = list(nums)
        self.index: int = 0

    def next(self) -> int:
        value = self.nums[self.index]
        self.index += 1
        return value

    def has_next(self) -> bool:
        return self.index < len(self.nums)


def run_peeking_iterator(solution_class: type, operations: list[str], inputs: list[list]):
    iterator = None
    results: list[int | bool | None] = []
    for i, op in enumerate(operations):
        if op == "PeekingIterator":
            iterator = solution_class(Iterator(inputs[i][0]))
            results.append(None)
        elif op == "next" and iterator is not None:
            results.append(iterator.next())
        elif op == "peek" and iterator is not None:
            results.append(iterator.peek())
        elif op == "has_next" and iterator is not None:
            results.append(iterator.has_next())
    return results, iterator


def assert_peeking_iterator(
    result: list[int | bool | None], expected: list[int | bool | None]
) -> bool:
    assert result == expected
    return True
