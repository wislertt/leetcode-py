from typing import Any


def run_shuffle_operations(solution_class: type, nums: list[int], operations: list[str]):
    obj: Any = None
    results: list[list[int] | None] = []
    for op in operations:
        if op == "Solution":
            obj = solution_class(nums)
        elif op == "reset" and obj is not None:
            results.append(obj.reset())
        elif op == "shuffle" and obj is not None:
            results.append(obj.shuffle())
    return results, obj


def assert_shuffle_operations(
    result: list[list[int] | None], expected: list[list[int] | None], nums: list[int]
) -> bool:
    assert len(result) == len(expected)
    for got, exp in zip(result, expected, strict=True):
        if exp is None:
            assert got is not None
            assert sorted(got) == sorted(nums)
        else:
            assert got == exp
    return True
