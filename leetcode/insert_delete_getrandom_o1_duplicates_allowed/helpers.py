from typing import Any


def run_randomized_collection_operations(
    solution_class: type, operations: list[str], inputs: list[list[int]]
):
    obj: Any = None
    results: list[int | bool | None] = []
    for i, op in enumerate(operations):
        if op == "RandomizedCollection":
            obj = solution_class()
            results.append(None)
        elif op == "insert" and obj is not None:
            results.append(obj.insert(inputs[i][0]))
        elif op == "remove" and obj is not None:
            results.append(obj.remove(inputs[i][0]))
        elif op == "getRandom" and obj is not None:
            results.append(obj.get_random())
    return results


def assert_randomized_collection_operations(
    result: list[int | bool | None], expected: list[int | bool | None]
) -> bool:
    assert result == expected
    return True
