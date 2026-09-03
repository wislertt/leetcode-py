def run_rle_iterator(solution_class: type, operations: list[str], inputs: list[list[int]]):
    iterator = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "RLEIterator":
            iterator = solution_class(inputs[i])
            results.append(None)
        elif op == "next" and iterator is not None:
            results.append(iterator.next(inputs[i][0]))
    return results, iterator


def assert_rle_iterator(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
