def run_append_characters(solution_class: type, s: str, t: str):
    implementation = solution_class()
    return implementation.append_characters(s, t)


def assert_append_characters(result: int, expected: int) -> bool:
    assert result == expected
    return True
