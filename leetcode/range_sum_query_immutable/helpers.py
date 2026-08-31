from typing import Any


def run_range_sum_query_immutable(
    solution_class: type, operations: list[str], inputs: list[list[Any]]
):
    num_array: Any = None
    results: list[Any] = []

    for op, args in zip(operations, inputs, strict=False):
        if op == "NumArray":
            num_array = solution_class(args[0])
            results.append(None)
        elif op == "sumRange":
            assert num_array is not None
            results.append(num_array.sum_range(args[0], args[1]))

    return results


def assert_range_sum_query_immutable(result: list[Any], expected: list[Any]) -> bool:
    assert result == expected
    return True
