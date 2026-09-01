def run_max_matrix_sum(solution_class: type, matrix: list[list[int]]):
    implementation = solution_class()
    return implementation.max_matrix_sum(matrix)


def assert_max_matrix_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
