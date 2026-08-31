def run_count_of_atoms(solution_class: type, formula: str):
    implementation = solution_class()
    return implementation.count_of_atoms(formula)


def assert_count_of_atoms(result: str, expected: str) -> bool:
    assert result == expected
    return True
