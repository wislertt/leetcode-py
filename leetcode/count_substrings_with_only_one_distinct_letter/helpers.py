def run_count_letters(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.count_letters(s)


def assert_count_letters(result: int, expected: int) -> bool:
    assert result == expected
    return True
