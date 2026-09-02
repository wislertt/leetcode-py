def run_last_remaining(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.last_remaining(n)


def assert_last_remaining(result: int, expected: int) -> bool:
    assert result == expected
    return True
