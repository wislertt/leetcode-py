def run_longest_substring_with_at_least_k_repeating_characters(
    solution_class: type, s: str, k: int
):
    implementation = solution_class()
    return implementation.longest_substring_with_at_least_k_repeating_characters(s, k)


def assert_longest_substring_with_at_least_k_repeating_characters(
    result: int, expected: int
) -> bool:
    assert result == expected
    return True
