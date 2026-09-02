def run_words_typing(solution_class: type, sentence: list[str], rows: int, cols: int):
    implementation = solution_class()
    return implementation.words_typing(sentence, rows, cols)


def assert_words_typing(result: int, expected: int) -> bool:
    assert result == expected
    return True
