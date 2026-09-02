def run_max_score_words(
    solution_class: type, words: list[str], letters: list[str], score: list[int]
):
    implementation = solution_class()
    return implementation.max_score_words(words, letters, score)


def assert_max_score_words(result: int, expected: int) -> bool:
    assert result == expected
    return True
