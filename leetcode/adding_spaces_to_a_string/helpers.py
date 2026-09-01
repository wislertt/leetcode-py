def run_add_spaces(solution_class: type, s: str, spaces: list[int]):
    implementation = solution_class()
    return implementation.add_spaces(s, spaces)


def assert_add_spaces(result: str, expected: str) -> bool:
    assert result == expected
    return True
