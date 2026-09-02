def run_all_one(solution_class: type, operations: list[str], inputs: list[list[str]]):
    implementation = None
    results: list[str | None] = []
    for i, op in enumerate(operations):
        if op == "AllOne":
            implementation = solution_class()
            results.append(None)
        elif op == "inc" and implementation is not None:
            implementation.inc(inputs[i][0])
            results.append(None)
        elif op == "dec" and implementation is not None:
            implementation.dec(inputs[i][0])
            results.append(None)
        elif op == "get_max_key" and implementation is not None:
            results.append(implementation.get_max_key())
        elif op == "get_min_key" and implementation is not None:
            results.append(implementation.get_min_key())
    return results, implementation


def assert_all_one(result: list[str | None], expected: list[str | None]) -> bool:
    assert result == expected
    return True
