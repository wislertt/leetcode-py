def run_subarrays_div_by_k(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.subarrays_div_by_k(nums, k)


def assert_subarrays_div_by_k(result: int, expected: int) -> bool:
    assert result == expected
    return True
