def run_common_chars(solution_class: type, words: list[str]):
    implementation = solution_class()
    return implementation.common_chars(words)


def assert_common_chars(result: list[str], expected: list[str]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
