def run_zigzag_iterator(solution_class: type, operations: list[str], inputs: list[list]):
    iterator = None
    results: list[int | bool | None] = []
    for i, op in enumerate(operations):
        if op == "ZigzagIterator":
            iterator = solution_class(inputs[i][0], inputs[i][1])
            results.append(None)
        elif op == "next" and iterator is not None:
            results.append(iterator.next())
        elif op == "has_next" and iterator is not None:
            results.append(iterator.has_next())
    return results, iterator


def assert_zigzag_iterator(
    result: list[int | bool | None], expected: list[int | bool | None]
) -> bool:
    assert result == expected
    return True
