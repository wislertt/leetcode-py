def run_word_pattern(solution_class: type, pattern: str, s: str):
    implementation = solution_class()
    return implementation.word_pattern(pattern, s)


def assert_word_pattern(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
