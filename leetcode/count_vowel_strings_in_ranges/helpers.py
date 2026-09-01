def run_vowel_strings(solution_class: type, words: list[str], queries: list[list[int]]):
    implementation = solution_class()
    return implementation.vowel_strings(words, queries)


def assert_vowel_strings(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
