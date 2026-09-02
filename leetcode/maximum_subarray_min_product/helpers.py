def run_max_sum_min_product(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.max_sum_min_product(nums)


def assert_max_sum_min_product(result: int, expected: int) -> bool:
    assert result == expected
    return True
