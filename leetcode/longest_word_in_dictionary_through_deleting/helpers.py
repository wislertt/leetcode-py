def run_find_longest_word(solution_class: type, s: str, dictionary: list[str]):
    implementation = solution_class()
    return implementation.find_longest_word(s, dictionary)


def assert_find_longest_word(result: str, expected: str) -> bool:
    assert result == expected
    return True
