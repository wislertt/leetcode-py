def run_calc_equation(
    solution_class: type, equations: list[list[str]], values: list[float], queries: list[list[str]]
):
    implementation = solution_class()
    return implementation.calc_equation(equations, values, queries)


def assert_calc_equation(result: list[float], expected: list[float]) -> bool:
    assert result == expected
    return True
