def run_valid_word_square(solution_class: type, words: list[str]):
    implementation = solution_class()
    return implementation.valid_word_square(words)


def assert_valid_word_square(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
