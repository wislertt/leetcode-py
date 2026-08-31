def run_spiral_matrix_iii(solution_class: type, rows: int, cols: int, r_start: int, c_start: int):
    implementation = solution_class()
    return implementation.spiral_matrix_iii(rows, cols, r_start, c_start)


def assert_spiral_matrix_iii(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
