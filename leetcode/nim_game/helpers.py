def run_can_win_nim(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.can_win_nim(n)


def assert_can_win_nim(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
