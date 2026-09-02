def run_parse_ternary(solution_class: type, expression: str):
    implementation = solution_class()
    return implementation.parse_ternary(expression)


def assert_parse_ternary(result: str, expected: str) -> bool:
    assert result == expected
    return True
