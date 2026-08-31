from typing import Any


def run_depth_sum_inverse(solution_class: type, nested_list: list[Any]):
    implementation = solution_class()
    return implementation.depth_sum_inverse(nested_list)


def assert_depth_sum_inverse(result: int, expected: int) -> bool:
    assert result == expected
    return True
