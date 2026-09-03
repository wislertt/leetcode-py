def run_reordered_power_of_2(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.reordered_power_of_2(n)


def assert_reordered_power_of_2(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
