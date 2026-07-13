from typing import Any


def run_random_pick_operations(
    solution_class: type, operations: list[str], inputs: list[list[int]]
):
    obj: Any = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "Solution":
            obj = solution_class(inputs[i][0])
            results.append(None)
        elif op == "pickIndex" and obj is not None:
            results.append(obj.pick_index())
    return results


def assert_random_pick_operations(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
