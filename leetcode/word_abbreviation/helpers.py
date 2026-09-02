def run_words_abbreviation(solution_class: type, words: list[str]):
    implementation = solution_class()
    return implementation.words_abbreviation(words)


def assert_words_abbreviation(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True
