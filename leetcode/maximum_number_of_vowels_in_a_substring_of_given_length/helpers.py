def run_max_vowels(solution_class: type, s: str, k: int):
    implementation = solution_class()
    return implementation.max_vowels(s, k)


def assert_max_vowels(result: int, expected: int) -> bool:
    assert result == expected
    return True
