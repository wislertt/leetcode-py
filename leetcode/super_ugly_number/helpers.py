def run_nth_super_ugly_number(solution_class: type, n: int, primes: list[int]):
    implementation = solution_class()
    return implementation.nth_super_ugly_number(n, primes)


def assert_nth_super_ugly_number(result: int, expected: int) -> bool:
    assert result == expected
    return True
