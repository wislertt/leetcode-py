from typing import Any


def run_kth_largest(solution_class: type, operations: list[str], inputs: list[list[Any]]):
    kth: Any = None
    results: list[Any] = []

    for op, args in zip(operations, inputs, strict=False):
        if op == "KthLargest":
            kth = solution_class(args[0], args[1])
            results.append(None)
        elif op == "add":
            assert kth is not None
            results.append(kth.add(args[0]))

    return results


def assert_kth_largest(result: list[Any], expected: list[Any]) -> bool:
    assert result == expected
    return True
