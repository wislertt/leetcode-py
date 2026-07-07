def run_longest_valid_parentheses(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.longest_valid_parentheses(s)


def assert_longest_valid_parentheses(result: int, expected: int) -> bool:
    assert result == expected
    return True
