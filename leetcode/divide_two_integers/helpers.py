def run_divide(solution_class: type, dividend: int, divisor: int):
    implementation = solution_class()
    return implementation.divide(dividend, divisor)


def assert_divide(result: int, expected: int) -> bool:
    assert result == expected
    return True
