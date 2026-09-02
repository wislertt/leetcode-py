def run_maximal_rectangle(solution_class: type, matrix: list[list[str]]):
    implementation = solution_class()
    return implementation.maximal_rectangle(matrix)


def assert_maximal_rectangle(result: int, expected: int) -> bool:
    assert result == expected
    return True
