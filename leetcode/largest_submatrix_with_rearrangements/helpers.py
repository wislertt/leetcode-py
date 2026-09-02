def run_largest_submatrix(solution_class: type, matrix: list[list[int]]):
    implementation = solution_class()
    return implementation.largest_submatrix(matrix)


def assert_largest_submatrix(result: int, expected: int) -> bool:
    assert result == expected
    return True
