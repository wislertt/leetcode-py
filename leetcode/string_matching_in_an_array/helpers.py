def run_string_matching(solution_class: type, words: list[str]):
    implementation = solution_class()
    return implementation.string_matching(words)


def assert_string_matching(result: list[str], expected: list[str]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
