def run_is_perfect_square(solution_class: type, num: int):
    implementation = solution_class()
    return implementation.is_perfect_square(num)


def assert_is_perfect_square(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
