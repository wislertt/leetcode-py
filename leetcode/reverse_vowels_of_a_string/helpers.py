def run_reverse_vowels(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.reverse_vowels(s)


def assert_reverse_vowels(result: str, expected: str) -> bool:
    assert result == expected
    return True
