def run_can_reach(solution_class: type, s: str, min_jump: int, max_jump: int):
    implementation = solution_class()
    return implementation.can_reach(s, min_jump, max_jump)


def assert_can_reach(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
