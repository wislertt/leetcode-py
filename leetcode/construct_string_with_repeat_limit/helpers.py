def run_repeat_limited_string(solution_class: type, s: str, repeat_limit: int):
    implementation = solution_class()
    return implementation.repeat_limited_string(s, repeat_limit)


def assert_repeat_limited_string(result: str, expected: str) -> bool:
    assert result == expected
    return True
