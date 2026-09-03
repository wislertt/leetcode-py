def run_fraction_addition(solution_class: type, expression: str):
    implementation = solution_class()
    return implementation.fraction_addition(expression)


def assert_fraction_addition(result: str, expected: str) -> bool:
    assert result == expected
    return True
