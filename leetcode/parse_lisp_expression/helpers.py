def run_evaluate(solution_class: type, expression: str):
    implementation = solution_class()
    return implementation.evaluate(expression)


def assert_evaluate(result: int, expected: int) -> bool:
    assert result == expected
    return True
