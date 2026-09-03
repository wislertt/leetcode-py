def run_longest_line(solution_class: type, mat: list[list[int]]):
    implementation = solution_class()
    return implementation.longest_line(mat)


def assert_longest_line(result: int, expected: int) -> bool:
    assert result == expected
    return True
