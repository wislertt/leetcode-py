def run_reverse_words(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.reverse_words(s)


def assert_reverse_words(result: str, expected: str) -> bool:
    assert result == expected
    return True
