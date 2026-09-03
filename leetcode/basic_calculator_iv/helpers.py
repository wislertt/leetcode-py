def run_basic_calculator_iv(
    solution_class: type, expression: str, evalvars: list[str], evalints: list[int]
):
    implementation = solution_class()
    return implementation.basic_calculator_iv(expression, evalvars, evalints)


def assert_basic_calculator_iv(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True
