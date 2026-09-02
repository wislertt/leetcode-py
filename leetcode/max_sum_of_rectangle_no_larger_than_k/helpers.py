def run_max_sum_submatrix(solution_class: type, matrix: list[list[int]], k: int):
    implementation = solution_class()
    return implementation.max_sum_submatrix(matrix, k)


def assert_max_sum_submatrix(result: int, expected: int) -> bool:
    assert result == expected
    return True
