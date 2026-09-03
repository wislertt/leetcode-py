def run_score_of_parentheses(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.score_of_parentheses(s)


def assert_score_of_parentheses(result: int, expected: int) -> bool:
    assert result == expected
    return True
