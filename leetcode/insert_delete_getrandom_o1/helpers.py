from typing import Any


def run_randomized_set_operations(
    solution_class: type, operations: list[str], inputs: list[list[int]]
):
    obj: Any = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "RandomizedSet":
            obj = solution_class()
            results.append(None)
        elif op == "insert" and obj is not None:
            results.append(obj.insert(inputs[i][0]))
        elif op == "remove" and obj is not None:
            results.append(obj.remove(inputs[i][0]))
        elif op == "getRandom" and obj is not None:
            results.append(obj.get_random())
    return results


def assert_randomized_set_operations(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
