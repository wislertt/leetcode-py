def run_diagonal_sum(solution_class: type, mat: list[list[int]]):
    implementation = solution_class()
    return implementation.diagonal_sum(mat)


def assert_diagonal_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
