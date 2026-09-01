def run_closest_primes(solution_class: type, left: int, right: int):
    implementation = solution_class()
    return implementation.closest_primes(left, right)


def assert_closest_primes(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
