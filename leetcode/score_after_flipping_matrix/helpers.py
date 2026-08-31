def run_matrix_score(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.matrix_score(grid)


def assert_matrix_score(result: int, expected: int) -> bool:
    assert result == expected
    return True
