def run_first_uniq_char(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.first_uniq_char(s)


def assert_first_uniq_char(result: int, expected: int) -> bool:
    assert result == expected
    return True
