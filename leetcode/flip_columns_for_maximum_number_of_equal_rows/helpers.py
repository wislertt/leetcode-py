def run_max_equal_rows_after_flips(solution_class: type, matrix: list[list[int]]):
    implementation = solution_class()
    return implementation.max_equal_rows_after_flips(matrix)


def assert_max_equal_rows_after_flips(result: int, expected: int) -> bool:
    assert result == expected
    return True
