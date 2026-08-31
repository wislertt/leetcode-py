def run_count_squares(solution_class: type, matrix: list[list[int]]):
    implementation = solution_class()
    return implementation.count_squares(matrix)


def assert_count_squares(result: int, expected: int) -> bool:
    assert result == expected
    return True
