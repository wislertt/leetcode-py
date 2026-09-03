def run_solve_equation(solution_class: type, equation: str):
    implementation = solution_class()
    return implementation.solve_equation(equation)


def assert_solve_equation(result: str, expected: str) -> bool:
    assert result == expected
    return True
