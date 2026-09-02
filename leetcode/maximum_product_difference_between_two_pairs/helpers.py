def run_max_product_difference(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.max_product_difference(nums)


def assert_max_product_difference(result: int, expected: int) -> bool:
    assert result == expected
    return True
