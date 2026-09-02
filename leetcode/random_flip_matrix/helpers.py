from typing import Any


def run_flip_operations(solution_class: type, m: int, n: int, operations: list[str]):
    obj: Any = None
    results: list[list[int] | None] = []
    for op in operations:
        if op == "Solution":
            obj = solution_class(m, n)
        elif op == "flip" and obj is not None:
            results.append(obj.flip())
        elif op == "reset" and obj is not None:
            results.append(obj.reset())
    return results, obj


def assert_flip_operations(
    result: list[list[int] | None], expected: list[list[int] | None], m: int, n: int
) -> bool:
    assert len(result) == len(expected)
    seen: set[tuple[int, int]] = set()
    for got, exp in zip(result, expected, strict=True):
        if got is None:
            seen.clear()
        else:
            assert len(got) == 2
            assert 0 <= got[0] < m
            assert 0 <= got[1] < n
            assert (got[0], got[1]) not in seen
            seen.add((got[0], got[1]))
        if exp is not None:
            assert got == exp
    return True
