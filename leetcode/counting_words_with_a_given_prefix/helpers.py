def run_prefix_count(solution_class: type, words: list[str], pref: str):
    implementation = solution_class()
    return implementation.prefix_count(words, pref)


def assert_prefix_count(result: int, expected: int) -> bool:
    assert result == expected
    return True
