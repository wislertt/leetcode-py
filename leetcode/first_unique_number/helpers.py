def run_first_unique(solution_class: type, operations: list[str], inputs: list[list[int]]):
    first_unique = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "FirstUnique":
            first_unique = solution_class(inputs[i])
            results.append(None)
        elif op == "show_first_unique" and first_unique is not None:
            results.append(first_unique.show_first_unique())
        elif op == "add" and first_unique is not None:
            first_unique.add(inputs[i][0])
            results.append(None)
    return results, first_unique


def assert_first_unique(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
