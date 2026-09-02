def run_integer_replacement(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.integer_replacement(n)


def assert_integer_replacement(result: int, expected: int) -> bool:
    assert result == expected
    return True
