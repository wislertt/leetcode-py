def run_word_pattern_match(solution_class: type, pattern: str, s: str):
    implementation = solution_class()
    return implementation.word_pattern_match(pattern, s)


def assert_word_pattern_match(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
