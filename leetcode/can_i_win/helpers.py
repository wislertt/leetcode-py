def run_can_i_win(solution_class: type, max_choosable_integer: int, desired_total: int):
    implementation = solution_class()
    return implementation.can_i_win(max_choosable_integer, desired_total)


def assert_can_i_win(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
