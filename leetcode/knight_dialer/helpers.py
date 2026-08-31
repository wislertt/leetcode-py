def run_knight_dialer(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.knight_dialer(n)


def assert_knight_dialer(result: int, expected: int) -> bool:
    assert result == expected
    return True
