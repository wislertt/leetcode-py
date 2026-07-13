def run_my_stack(solution_class: type, operations: list[str], inputs: list[list[int]]):
    stack = None
    results: list[int | None | bool] = []
    for i, op in enumerate(operations):
        if op == "MyStack":
            stack = solution_class()
            results.append(None)
        elif op == "push" and stack is not None:
            stack.push(inputs[i][0])
            results.append(None)
        elif op == "pop" and stack is not None:
            results.append(stack.pop())
        elif op == "top" and stack is not None:
            results.append(stack.top())
        elif op == "empty" and stack is not None:
            results.append(stack.empty())
    return results, stack


def assert_my_stack(result: list[int | None | bool], expected: list[int | None | bool]) -> bool:
    assert result == expected
    return True
