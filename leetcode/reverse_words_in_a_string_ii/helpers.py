def run_reverse_words(solution_class: type, s: list[str]):
    implementation = solution_class()
    implementation.reverse_words(s)
    return s


def assert_reverse_words(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True
