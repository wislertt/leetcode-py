def run_num_submatrix_sum_target(solution_class: type, matrix: list[list[int]], target: int):
    implementation = solution_class()
    return implementation.num_submatrix_sum_target(matrix, target)


def assert_num_submatrix_sum_target(result: int, expected: int) -> bool:
    assert result == expected
    return True
