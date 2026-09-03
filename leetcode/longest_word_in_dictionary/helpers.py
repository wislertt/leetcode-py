def run_longest_word(solution_class: type, words: list[str]):
    implementation = solution_class()
    return implementation.longest_word(words)


def assert_longest_word(result: str, expected: str) -> bool:
    assert result == expected
    return True
