def run_count_binary_substrings(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.count_binary_substrings(s)


def assert_count_binary_substrings(result: int, expected: int) -> bool:
    assert result == expected
    return True
