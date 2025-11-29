from typing import List


def run_generate(solution_class: type, numRows: int):
    implementation = solution_class()
    return implementation.generate(numRows)


def assert_generate(result: List[List[int]], expected: List[List[int]]) -> bool:
    assert result == expected
    return True
