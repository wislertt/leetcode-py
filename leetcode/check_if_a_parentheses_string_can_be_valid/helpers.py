def run_can_be_valid(solution_class: type, s: str, locked: str):
    implementation = solution_class()
    return implementation.can_be_valid(s, locked)


def assert_can_be_valid(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
