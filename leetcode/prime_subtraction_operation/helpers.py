def run_prime_sub_operation(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.prime_sub_operation(nums)


def assert_prime_sub_operation(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
