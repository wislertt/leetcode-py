def run_integer_break(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.integer_break(n)


def assert_integer_break(result: int, expected: int) -> bool:
    assert result == expected
    return True
