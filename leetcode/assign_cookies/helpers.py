from typing import List


def run_find_content_children(solution_class: type, g: List[int], s: List[int]):
    implementation = solution_class()
    return implementation.find_content_children(g, s)


def assert_find_content_children(result: int, expected: int) -> bool:
    assert result == expected
    return True
