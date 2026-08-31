def run_count_primes(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.count_primes(n)


def assert_count_primes(result: int, expected: int) -> bool:
    assert result == expected
    return True
