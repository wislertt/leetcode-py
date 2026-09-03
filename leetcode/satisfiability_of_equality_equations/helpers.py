def run_equations_possible(solution_class: type, equations: list[str]):
    implementation = solution_class()
    return implementation.equations_possible(equations)


def assert_equations_possible(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
