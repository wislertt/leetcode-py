def run_map_sum(solution_class: type, operations: list[str], inputs: list[list]):
    map_sum = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "MapSum":
            map_sum = solution_class()
            results.append(None)
        elif op == "insert" and map_sum is not None:
            map_sum.insert(*inputs[i])
            results.append(None)
        elif op == "sum" and map_sum is not None:
            results.append(map_sum.sum(*inputs[i]))
    return results, map_sum


def assert_map_sum(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
