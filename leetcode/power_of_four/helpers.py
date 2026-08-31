def run_is_power_of_four(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.is_power_of_four(n)


def assert_is_power_of_four(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
