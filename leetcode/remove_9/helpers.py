def run_new_integer(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.new_integer(n)


def assert_new_integer(result: int, expected: int) -> bool:
    assert result == expected
    return True
