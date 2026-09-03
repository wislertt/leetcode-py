def run_replace_words(solution_class: type, dictionary: list[str], sentence: str):
    implementation = solution_class()
    return implementation.replace_words(dictionary, sentence)


def assert_replace_words(result: str, expected: str) -> bool:
    assert result == expected
    return True
