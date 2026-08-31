def run_can_win(solution_class: type, current_state: str):
    implementation = solution_class()
    return implementation.can_win(current_state)


def assert_can_win(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
