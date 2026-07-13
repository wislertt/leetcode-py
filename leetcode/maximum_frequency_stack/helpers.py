from typing import Any


def run_freq_stack_operations(solution_class: type, operations: list[str], inputs: list[list[int]]):
    stack: Any = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "FreqStack":
            stack = solution_class()
            results.append(None)
        elif op == "push" and stack is not None:
            stack.push(inputs[i][0])
            results.append(None)
        elif op == "pop" and stack is not None:
            results.append(stack.pop())
    return results


def assert_freq_stack_operations(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
