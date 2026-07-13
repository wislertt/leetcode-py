def run_num_squares(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.num_squares(n)


def assert_num_squares(result: int, expected: int) -> bool:
    assert result == expected
    return True
