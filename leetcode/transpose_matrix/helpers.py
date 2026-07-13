def run_transpose(solution_class: type, matrix: list[list[int]]):
    implementation = solution_class()
    return implementation.transpose(matrix)


def assert_transpose(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
