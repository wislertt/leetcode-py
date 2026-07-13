def run_is_alien_sorted(solution_class: type, words: list[str], order: str):
    implementation = solution_class()
    return implementation.is_alien_sorted(words, order)


def assert_is_alien_sorted(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
