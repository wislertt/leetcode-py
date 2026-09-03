def run_kth_smallest_prime_fraction(solution_class: type, arr: list[int], k: int):
    implementation = solution_class()
    return implementation.kth_smallest_prime_fraction(arr, k)


def assert_kth_smallest_prime_fraction(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
