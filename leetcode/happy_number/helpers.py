def run_is_happy(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.is_happy(n)


def assert_is_happy(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
