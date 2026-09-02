def run_fraction_to_decimal(solution_class: type, numerator: int, denominator: int):
    implementation = solution_class()
    return implementation.fraction_to_decimal(numerator, denominator)


def assert_fraction_to_decimal(result: str, expected: str) -> bool:
    assert result == expected
    return True
