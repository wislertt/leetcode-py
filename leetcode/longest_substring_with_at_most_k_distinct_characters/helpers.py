def run_length_of_longest_substring_k_distinct(solution_class: type, s: str, k: int):
    implementation = solution_class()
    return implementation.length_of_longest_substring_k_distinct(s, k)


def assert_length_of_longest_substring_k_distinct(result: int, expected: int) -> bool:
    assert result == expected
    return True
