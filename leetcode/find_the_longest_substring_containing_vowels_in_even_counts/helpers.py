def run_find_the_longest_substring(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.find_the_longest_substring(s)


def assert_find_the_longest_substring(result: int, expected: int) -> bool:
    assert result == expected
    return True
