def run_find_and_replace_pattern(solution_class: type, words: list[str], pattern: str):
    implementation = solution_class()
    return implementation.find_and_replace_pattern(words, pattern)


def assert_find_and_replace_pattern(result: list[str], expected: list[str]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
