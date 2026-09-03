def run_bold_words(solution_class: type, words: list[str], s: str):
    implementation = solution_class()
    return implementation.bold_words(words, s)


def assert_bold_words(result: str, expected: str) -> bool:
    assert result == expected
    return True
