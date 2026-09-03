def run_broken_calc(solution_class: type, start_value: int, target: int):
    implementation = solution_class()
    return implementation.broken_calc(start_value, target)


def assert_broken_calc(result: int, expected: int) -> bool:
    assert result == expected
    return True
