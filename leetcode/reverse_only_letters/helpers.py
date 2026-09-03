def run_reverse_only_letters(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.reverse_only_letters(s)


def assert_reverse_only_letters(result: str, expected: str) -> bool:
    assert result == expected
    return True
