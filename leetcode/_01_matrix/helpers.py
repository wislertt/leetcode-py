from typing import List


def run_update_matrix(solution_class: type, mat: List[List[int]]):
    implementation = solution_class()
    return implementation.update_matrix(mat)


def assert_update_matrix(result: List[List[int]], expected: List[List[int]]) -> bool:
    assert result == expected
    return True
