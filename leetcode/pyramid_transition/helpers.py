def run_pyramid_transition(solution_class: type, bottom: str, allowed: list[str]):
    implementation = solution_class()
    return implementation.pyramid_transition(bottom, allowed)


def assert_pyramid_transition(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
