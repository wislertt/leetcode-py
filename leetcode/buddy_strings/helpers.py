def run_buddy_strings(solution_class: type, s: str, goal: str):
    implementation = solution_class()
    return implementation.buddy_strings(s, goal)


def assert_buddy_strings(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
