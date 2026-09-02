def run_expand(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.expand(s)


def assert_expand(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True
