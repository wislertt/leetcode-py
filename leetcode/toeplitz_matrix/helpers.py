def run_is_toeplitz_matrix(solution_class: type, matrix: list[list[int]]):
    implementation = solution_class()
    return implementation.is_toeplitz_matrix(matrix)


def assert_is_toeplitz_matrix(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
