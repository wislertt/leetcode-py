def run_subarrays_with_k_distinct(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.subarrays_with_k_distinct(nums, k)


def assert_subarrays_with_k_distinct(result: int, expected: int) -> bool:
    assert result == expected
    return True
