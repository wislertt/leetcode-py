def run_is_scramble(solution_class: type, s1: str, s2: str):
    implementation = solution_class()
    return implementation.is_scramble(s1, s2)


def assert_is_scramble(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
