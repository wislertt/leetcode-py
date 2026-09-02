def run_minimum_one_bit_operations(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.minimum_one_bit_operations(n)


def assert_minimum_one_bit_operations(result: int, expected: int) -> bool:
    assert result == expected
    return True
