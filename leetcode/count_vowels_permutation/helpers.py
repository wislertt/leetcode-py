def run_count_vowel_permutation(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.count_vowel_permutation(n)


def assert_count_vowel_permutation(result: int, expected: int) -> bool:
    assert result == expected
    return True
