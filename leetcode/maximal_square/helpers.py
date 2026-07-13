def run_maximal_square(solution_class: type, matrix: list[list[str]]):
    implementation = solution_class()
    return implementation.maximal_square(matrix)


def assert_maximal_square(result: int, expected: int) -> bool:
    assert result == expected
    return True
