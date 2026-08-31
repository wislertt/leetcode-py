def run_reverse_parentheses(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.reverse_parentheses(s)


def assert_reverse_parentheses(result: str, expected: str) -> bool:
    assert result == expected
    return True
