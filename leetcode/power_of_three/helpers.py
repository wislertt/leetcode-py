def run_is_power_of_three(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.is_power_of_three(n)


def assert_is_power_of_three(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
