def run_rotate_string(solution_class: type, s: str, goal: str):
    implementation = solution_class()
    return implementation.rotate_string(s, goal)


def assert_rotate_string(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
