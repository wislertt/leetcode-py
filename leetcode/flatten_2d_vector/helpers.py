def run_flatten_2d_vector(solution_class: type, operations: list[str], inputs: list[list]):
    iterator = None
    results: list[int | bool | None] = []
    for i, op in enumerate(operations):
        if op == "Vector2D":
            iterator = solution_class(inputs[i])
            results.append(None)
        elif op == "next" and iterator is not None:
            results.append(iterator.next())
        elif op == "has_next" and iterator is not None:
            results.append(iterator.has_next())
    return results, iterator


def assert_flatten_2d_vector(
    result: list[int | bool | None], expected: list[int | bool | None]
) -> bool:
    assert result == expected
    return True
