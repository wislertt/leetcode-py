def run_remove_invalid_parentheses(solution_class: type, s: str):
    implementation = solution_class()
    return sorted(implementation.remove_invalid_parentheses(s))


def assert_remove_invalid_parentheses(result: list[str], expected: list[str]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
