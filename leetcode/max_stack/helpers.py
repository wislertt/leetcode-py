def run_max_stack(solution_class: type, operations: list[str], inputs: list[list[int]]):
    stack = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "MaxStack":
            stack = solution_class()
            results.append(None)
        elif op == "push" and stack is not None:
            stack.push(inputs[i][0])
            results.append(None)
        elif stack is not None:
            results.append(getattr(stack, op)())
    return results, stack


def assert_max_stack(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
