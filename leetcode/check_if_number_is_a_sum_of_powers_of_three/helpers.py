def run_check_powers_of_three(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.check_powers_of_three(n)


def assert_check_powers_of_three(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
