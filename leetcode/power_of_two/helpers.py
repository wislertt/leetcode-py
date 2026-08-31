def run_is_power_of_two(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.is_power_of_two(n)


def assert_is_power_of_two(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
