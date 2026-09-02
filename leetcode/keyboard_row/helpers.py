def run_find_words(solution_class: type, words: list[str]):
    implementation = solution_class()
    return implementation.find_words(words)


def assert_find_words(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True
