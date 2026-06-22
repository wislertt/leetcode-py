from typing import Any


def run_detect_squares(solution_class: type, operations: list[str], inputs: list[Any]):
    squares: Any = None
    results: list[Any] = []

    for op, args in zip(operations, inputs, strict=False):
        if op == "DetectSquares":
            squares = solution_class()
            results.append(None)
        elif op == "add":
            assert squares is not None
            squares.add(args[0])
            results.append(None)
        elif op == "count":
            assert squares is not None
            results.append(squares.count(args[0]))

    return results


def assert_detect_squares(result: list[Any], expected: list[Any]) -> bool:
    assert result == expected
    return True
