def run_array_strings_are_equal(solution_class: type, word1: list[str], word2: list[str]):
    implementation = solution_class()
    return implementation.array_strings_are_equal(word1, word2)


def assert_array_strings_are_equal(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
