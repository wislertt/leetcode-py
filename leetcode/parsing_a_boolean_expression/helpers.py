def run_parse_bool_expr(solution_class: type, expression: str):
    implementation = solution_class()
    return implementation.parse_bool_expr(expression)


def assert_parse_bool_expr(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
