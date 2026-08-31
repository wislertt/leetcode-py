def run_num_subarray_product_less_than_k(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.num_subarray_product_less_than_k(nums, k)


def assert_num_subarray_product_less_than_k(result: int, expected: int) -> bool:
    assert result == expected
    return True
