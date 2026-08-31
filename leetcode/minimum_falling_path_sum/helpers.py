def run_min_falling_path_sum(solution_class: type, matrix: list[list[int]]):
    implementation = solution_class()
    return implementation.min_falling_path_sum(matrix)


def assert_min_falling_path_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
