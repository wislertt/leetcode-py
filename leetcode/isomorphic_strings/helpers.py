def run_is_isomorphic(solution_class: type, s: str, t: str):
    implementation = solution_class()
    return implementation.is_isomorphic(s, t)


def assert_is_isomorphic(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
