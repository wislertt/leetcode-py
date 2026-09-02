from typing import Any


def run_random_pick_index(solution_class: type, operations: list[str], inputs: list[list[int]]):
    obj: Any = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "Solution":
            obj = solution_class(inputs[i][0])
            results.append(None)
        elif op == "pick" and obj is not None:
            results.append(obj.pick(inputs[i][0]))
    return results


def assert_random_pick_index(result: list[int | None], expected: list[list[int | None]]) -> bool:
    assert len(result) == len(expected)
    for r, choices in zip(result, expected, strict=True):
        assert r in choices
    return True
