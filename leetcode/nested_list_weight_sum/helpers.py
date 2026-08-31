from typing import Any


def run_depth_sum(solution_class: type, nested_list: list[Any]):
    implementation = solution_class()
    return implementation.depth_sum(nested_list)


def assert_depth_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
