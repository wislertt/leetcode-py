def run_count_prime_set_bits(solution_class: type, left: int, right: int):
    implementation = solution_class()
    return implementation.count_prime_set_bits(left, right)


def assert_count_prime_set_bits(result: int, expected: int) -> bool:
    assert result == expected
    return True
