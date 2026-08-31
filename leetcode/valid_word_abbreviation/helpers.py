def run_valid_word_abbreviation(solution_class: type, word: str, abbr: str):
    implementation = solution_class()
    return implementation.valid_word_abbreviation(word, abbr)


def assert_valid_word_abbreviation(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
