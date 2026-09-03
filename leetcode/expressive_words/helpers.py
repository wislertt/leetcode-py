def run_expressive_words(solution_class: type, s: str, words: list[str]):
    implementation = solution_class()
    return implementation.expressive_words(s, words)


def assert_expressive_words(result: int, expected: int) -> bool:
    assert result == expected
    return True
