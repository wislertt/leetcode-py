def run_range_module(solution_class: type, operations: list[str], inputs: list[list[int]]):
    module = None
    results: list[bool | None] = []
    for i, op in enumerate(operations):
        if op == "RangeModule":
            module = solution_class()
            results.append(None)
        elif op == "add_range" and module is not None:
            module.add_range(inputs[i][0], inputs[i][1])
            results.append(None)
        elif op == "query_range" and module is not None:
            results.append(module.query_range(inputs[i][0], inputs[i][1]))
        elif op == "remove_range" and module is not None:
            module.remove_range(inputs[i][0], inputs[i][1])
            results.append(None)
    return results, module


def assert_range_module(result: list[bool | None], expected: list[bool | None]) -> bool:
    assert result == expected
    return True
