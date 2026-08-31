def run_string_iterator(solution_class: type, operations: list[str], inputs: list[list[str]]):
    iterator = None
    results: list[str | bool | None] = []
    for i, op in enumerate(operations):
        if op == "StringIterator":
            iterator = solution_class(inputs[i][0])
            results.append(None)
        elif op == "next" and iterator is not None:
            results.append(iterator.next())
        elif op == "has_next" and iterator is not None:
            results.append(iterator.has_next())
    return results, iterator


def assert_string_iterator(
    result: list[str | bool | None], expected: list[str | bool | None]
) -> bool:
    assert result == expected
    return True
