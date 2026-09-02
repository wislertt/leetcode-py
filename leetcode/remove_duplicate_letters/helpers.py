def run_remove_duplicate_letters(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.remove_duplicate_letters(s)


def assert_remove_duplicate_letters(result: str, expected: str) -> bool:
    assert result == expected
    return True
