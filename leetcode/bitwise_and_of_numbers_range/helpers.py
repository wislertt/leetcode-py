def run_range_bitwise_and(solution_class: type, left: int, right: int):
    implementation = solution_class()
    return implementation.range_bitwise_and(left, right)


def assert_range_bitwise_and(result: int, expected: int) -> bool:
    assert result == expected
    return True
